Common Tasks
------------

#### Page Blocks

A configurable object that would be rendered in a specified section of the page (as defined in its base template).
It can take a long Text as content, a json objects or whatever, it dependes by Block Type.
Examples:

- A pure HTML renderer
- A Specialized Block element that take a json object in its object constructor

The following descriptions covers some HTML blocks.
As we can see the HTML blocks in uniCMS have a full support of Django templatetags and template context.


*Load Image slider (Carousel) configured for the Page*
````
{% load unicms_carousels %}
{% load_carousel section='slider' template="unical_portale_hero.html" %}

<script>
$(document).ready(function() {
  $("#my-slider").owlCarousel({
      navigation : true, // Show next and prev buttons
      loop: true,
      slideSpeed : 300,
      paginationSpeed : 400,
      autoplay: true,
      items : 1,
      itemsDesktop : false,
      itemsDesktopSmall : false,
      itemsTablet: false,
      itemsMobile : false,
      dots: false
  });
});
</script>
````

*Load Publication preview in a Page*
it widely use the load_publications_preview templatetag, this 
template tags loads all the pubblication related to the WebPath (CMS Context) 
of the Page.

````
{% load unicms_blocks %}
    <div class="row negative-mt-5 mb-3" >
        <div class="col-12 col-md-3">
            <div class="section-title-label px-3 py-1">
                <h3>Unical <span class="super-bold">world</span></h3>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-12 col-lg-9">
            {% load_publications_preview template="publications_preview_v3.html" %}
        </div>
        <div class="col-12 col-lg-3">
            {% include "unical_portale_agenda.html" %}
        </div>
    </div>
````

*Youtube iframes*
As simple as possibile, that bunch of HTML lines.
````
<div class="row">
<div class="col-12 col-md-6">
<iframe width="100%" height="315" src="https://www.youtube.com/embed/ArpMSujC8mM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
 <div class="col-12 col-md-6">
<iframe width="100%" height="315" src="https://www.youtube.com/embed/xrjjJGqZpcU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
 </div>
````


#### Menu

A WebPath (context) can have multiple Menus and Navigation bars, but also Footers.
Menu can be fetched through Rest API `/api/menu/<menu_id:int>` and also updated/created through this resources.

Each menu items can have three kinds of links: url, page, publication.
Each menu items can get additional contents (`inherited_contents`) from a publication, this means that
a presentation url, or a subheading or whatever belonging to a publication can be made accessible during a 
menu items representation. Think about presentati in images, additional links ...


#### Urls

All the urls that matches the namespace configured in the `urls.py` of the master project
will be handled by uniCMS. uniCMS can match two kind of resources:

1. WebPath (Context) corresponsing at a single Page (Home page and its childs)
2. Application Handlers, an example would be Pubblication List and Views resources

for these latter uniCMS uses some reserved words, as prefix, to deal with specialized url routings.
in the settings file we would configure these. See [Handlers](#handlers) for example.

See `cms.contexts.settings` as example.
See `cms.contexts.views.cms_dispatcher` to see how an http request is intercepted and handled by uniCMS to know if use an Handler or a Standard Page as response.


#### Search Engine

uniCMS uses MongoDB as search engine, it was adopted in place of others search engines like Elastic Search or Sorl, for the following reasons:

- The documents stored are really small, few kilobytes (BSON storage)
- collections would be populated on each creation/change event by on_save hooks
- each entry is composed following a small schema, this would reduce storage usage increasing the performances at the same time

Technical specifications are available in [MongoDB Official Documentation](https://docs.mongodb.com/manual/core/index-text/).
Some usage example also have been posted [here](https://code.tutsplus.com/tutorials/full-text-search-in-mongodb--cms-24835).

An document would be as follows (see `cms.search.models`)

````
entry = {
            "title": "Papiri, Codex, Libri. La attraverso labora lorem ipsum",
            "heading": "Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.",
            "content_type": "cms.publications.Publication",
            "content_id": "1",
            "image": "/media/medias/2020/test_news_1.jpg",
            "content": "<p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?</p><p>&lt;h1&gt;This HTML is escaped by default!&lt;/h1&gt;</p><p>&nbsp;</p>",
            "sites": [
                "test.unical.it"
            ],
            "urls": [
                "//test.unical.it/portale/dipartimenti/dimes/contents/news/view/unical-campus-1",
                "//test.unical.it/portale/contents/news/view/unical-campus-1"
            ],
            "tags": [],
            "categories": [
                "Didattica"
            ],
            "indexed": "2020-12-09T15:00:18.151000",
            "published": "2020-11-09T13:24:35",
            "viewed": 0,
            "relevance": 0.5714285714285714,
            "language": "italian",
            "translations": [
                {
                    "language": "english",
                    "title": "gdfg",
                    "subheading": "dfgdfgdf",
                    "content": "<p>dfgdfgdfg</p>"
                }
            ],
            "day": 9,
            "month": 11,
            "year": 2020
        },
````

#### Search Engine CLI

Publication and Page models (`cms.publications.models`) configures by default some save_hooks, like the search engine indexers.
Search Engine indexes can be rebuilt with a management command (SE cli):

````
./manage.py cms_search_content_sync -y 2020 -type cmspublications.Publication -d 1 -y 2020 -m 11 -show
````

Purge all the entries and renew them
````
# all Pages
./manage.py cms_search_content_sync -y 2020 -type cmspages.Page -purge -insert -show

# everything in that year
./manage.py cms_search_content_sync  -purge -y 2020

# a single month
./manage.py cms_search_content_sync -y 2020 -type cmspublications.Publication -m 12 -y 2020 -purge -insert
````

`cms_search_content_sync` rely on `settings.MODEL_TO_MONGO_MAP`:
```
MODEL_TO_MONGO_MAP = {
    'cmspages.Page': 'cms.search.models.page_to_entry',
    'cmspublications.Publication': 'cms.search.models.publication_to_entry'
}
````

### Behavior

Let's suppose we are searching these words upon the previous entry.
These all matches:

- "my blog"
- "than reality"
- "rien la reliti"
- "my!"

These will not match:

- 'rien -"de plus"'
- '"my!"'
- '-nothing'

As we can see symbols like `+` and `-` will exlude or include words.
Specifying "some bunch of words" will match the entire sequence.
That's something very similar to something professional 😎.


#### Post Pre Save Hooks

By default Pages and Publications call pre and post save hooks.
Django signals are registered in `cms.contexts.signals`.
In `settings.py` we can register as many as desidered hooks to one or more 
models, Django signals will load them on each pre/post save/delete event.

````
CMS_HOOKS = {
    'Publication': {
        'PRESAVE': [],
        'POSTSAVE': ['cms.search.hooks.publication_se_insert',],
        'PREDELETE': ['cms.search.hooks.searchengine_entry_remove',],
        'POSTDELETE': []
    },
    'Page': {
        'PRESAVE': [],
        'POSTSAVE': ['cms.search.hooks.page_se_insert',],
        'PREDELETE': ['cms.search.hooks.searchengine_entry_remove',],
        'POSTDELETE': []
    }
}
```` 


#### Api

see `/openapi.json` and `/openapi` for OpenAPI v3 Schema.