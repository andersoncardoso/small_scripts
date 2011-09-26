Python | Ruby   <br/>   Django | Rails
==============          ===============

-----

The Life, The Universe <br/> and Everything Else !!
=======================      =======================

-----

Python and Ruby
===============

* High level languages
* Dynamic
    * static vs dynamic => bureaucratic vs agile
* Strong types 
    * Being dynamic, doesn't mean not having types
* Interpreted
* Multi-paradigm (OO, functional and structured)
* Best practices
* Faster/Easier to develop -> $$$
* Quite fun actually =D !!!

-----

Python
======
* from Monty Python...not the snake
* versions: Use 2.7 ... 3.x still not used in the market
* with Batteries included!
* simplicity
* great variety of uses:
    * desktop
    * Web
    * Computer Graphics
    * SysAdmin
    * You name it =]
    * also, this presentation =D
    
-----

Zen of Python
=============
Beautiful is better than ugly.  
**Explicit is better than implicit.**  
**Simple is better than complex.**  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
**There should be one-- and preferably only one --obvious way to do it.**  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than *right* now.  
**If the implementation is hard to explain, it's a bad idea.**  
**If the implementation is easy to explain, it may be a good idea.**  
**Namespaces are one honking great idea -- let's do more of those!**  

-----

Ruby
====

* beautiful (they say =/)
* very flexible (origins from perl)
* only really used in the web (RoR)
* great for DSLs
* Marketing !
* The ruby way
* Developed in Japan (the language core list is still in japanese =/...not good for OS)
* Matz is a great guy!
    * He sees what can be better and admit ruby flaws
    * different from DHH

-----

Who uses it? - Ruby
===================

**37 Signals** (criadores)  
**Groupon**  
**Twitter** (mudou backend para scala, mas front-end continua em RoR)  
**Github**  
shopiffy  
**yellow pages -> AT&T**  
Hulu  
scribd  
**justin.TV**  
SlideShare  
**Posterous**  
MTV  
Mix-**Oracle** -> pois é, nem a Oracle usa Java no seu site!!!  
Abril (BR)  
**Locaweb** (BR)  
Gonow (BR)  

-----

Who uses it? Python
===================

**Google**  
**youtube**  
NASA  
CIA  
**Mozilla**  
**Dropbox**  
**IL&M** (industrial light and magic)  
Disney   
**Disquss**   
**Reddit**  
Bitbuket  
**Globo.com** (BR)  
Yahoo (BR) (internacional tbm)  
Hipmunk, Yelp, Quora, Mixpanel (and most of big startups in the Valley)  
**FSF (Free Sofwtare Fundation)**    
Locaweb (BR)  
Predicta/BTBuckets (BR)  
**TVoD ... ;D  **

-----

Environments and Dependencies
=============================

* Python
    * virtualenv
    * pip  (python package installer)

* Ruby
    * rvm
    * gem 
    * bundler 

 
* No environment/dependencies headaches again
    * (yes... Im looking at you java-jar-hell >=( ...  )

-----

Language Characteristics - Ruby
===============================
    !ruby

        1.class 
        => Fixnum 

        class Fixnum 
            def +(outro) #very stupid monkey patch 
                42 
            end 
        end 

        1+1 
        => 42 

        5+0 
        => 42 

-----

Language Characteristics - Python
=================================
    !python
        type(1) 
        => <type 'int'>
        class int: 
            def __add__(self, outro): 
                return 42 # override da classe int ?  
        1+1 
        => 2 # e o nosso override??? 

        dir() 
        => ['__builtins__', '__doc__', '__name__', '__package__', 'int'] 
        # namespaces =D 
        n = int() 
        n + 1 
        => 42 
        type(n) 
        => <type 'instance'> 

        # e se eu quiser instancia um int sem literal? use seu namespace 
        n = __builtins__.int() 
        n+1 
        => 1 
        type(n) 
        => <type 'int'> 
        # namespaces == FUCK YEAH!!

-----

**Some APIs** <br/> go to redmine
=============       ==============

-----

IDEs
====

* We are not IDE operators!!!!!
    * (yes java Im looking at you again)
* Most of the hard core developers use vim/emacs
* Eclipse sucks....seriously
    * Not to say Aptana ...aaargh 
* If you want a fantastic IDE use jetbrains ones 
    * pycharm
    * Rubymine
    * Unfortunately they are proprietary...but it worths every cent...seriously! 
* Geany + plugins = more than enough

-----

Speed
======

* benchmarks sucks!! seriously!
* Python
    * pypy > python3 > python (cpython) >> jython
* Ruby
    * jruby > ruby1.9 > ruby 1.8 (mri)
* merging:
    * pypy > jruby > py3k > ruby1.9 >= python2.x > ruby1.8 >> jython

* In some cases pypy > C !!!!!
* again, its **not** an issue!

-----

Ruby on Rails
==============

* **Web development that doesn't hurt**
* Convention over Configuration
* magical (in the bad sense) internals
* "game changer" - changed the all web
* separates layers, physically (different folder and so)
* Opinionated -> BS 
* hype -> marketing (commercial appeal)
* DSL for the web 
* not so simple anymore (as in rails **3**)
* best practices -> migrations built-in, tests and etc
* fast development. We measure projects in days, maybe weeks. Not months. (for both Rails and Django)

-----

Django ( finally >=] )
======================

* **"The web framework for perfectionists with deadlines "**
* In one word?  **a-w-e-s-o-m-e!!! **
* Killer features:
    * Django admin
    * is in Python
    * **pluggable apps !!!!**
* Do not recreate the wheel ! **DRY**
    * DRYAO (don't repeat yourself and the others !)
* MTV (model - Views (controller) - Templates (view))
* Good scalability
* Obsessive about best practices


-----

Django - models
===============
  
<br/><br/>
models.py
<br/><br/>

    !python
        from django import models
        from django.contrib.auth.models import User
        
        class Task(models.Model):
            title = models.CharField('Titulo', max_length = 100)
            text = models.CharField('Tarefa', max_length = 400, null = True)
            owner = models.ForeignKey(User)
            pub_date = models.DateTimeField(auto_add_now = True)
            
            def __unicode__(self):
                return self.title

------

Django - views
==============

<br/><br/>
views.py
<br/><br/>

    !python
        from minhaapp.models import Task
        from django.shortcuts import render_to_response
        
        def task_list(request):
            task = Task.objects.all()[:5]  #lazy =]
            return render_to_response('tasklist.html', {'tasks':tasks})
            
        def task_details(request, tID=0):
            task = Task.objects.get(pk = tID)
            # task = get_object_or_404(Task, pk=tID)
            return render_to_response('taskdetails.html', {'task':task})

-----

Django - urls
=============

You can design you url as you wish, using RegExp.  

urls.py


    !python
        
        urlpatterns = pattterns('minhaapp.views', 
            url(r'^task/list/$', 'task_list'),
            url(r'^task/?P<tID>\d+/$', 'task_details'),
        )

     
generic views =]

    !python
        from django.views.generic import list_detail
        publisher_info = {
            "queryset" : Publisher.objects.all(),
            "paginate_by" : 10, 
            "template_name" : 'meu_template.html' #<app_label>/<model_name>_list.html by default.
        }
        urlpatterns = patterns('',
            (r'^publishers/page(?P<page>\d+)/$', list_detail.object_list, publisher_info),
            #publishers/?page=3
        )

-----

Django - templates
==================

<br/><br/>
base.html:
<br/><br/>

    !html
        <html>
            <head>
                <!-- bunch of js and css -->
            </head>
            <body>
              <!--cabeçalho e outras coisas -->
              <div id="content">
                  {% block content %} {% endblock %}
              </div>
            </body>
        </html>

<br/><br/>
OBS: templates are **HTML**!! (look the extension)

-----

Django - templates
==================

<br/><br/>
tasklist.html:
<br/><br/> 

    !html
        {% extends 'base.html' %}
 

        {% block content %}
            {% for task in tasks %}
             <div id="task{{ task.id }}">
                <h2>{{task.title}}</h2> - {{ task.pub_date|date:"d/m/Y" }}
                <a href="/task/{{ task.id }}" >details</a>
             </div>
            {% endfor %}
        {% endblock %}

<br/><br/>
OBS: templates are **HTML**!! (look the extension)

----

Django - templates
==================

<br/><br/>
taskdetails.html
<br/><br/>
    
    !html
        {% extends 'base.html' %}

        {% block content %}
             <div id="taskdetail">
                <h2>{{task.title}}</h2> - {{ task.pub_date|date:"d/m/Y" }}
                <p> {{task.text}} </p>
             </div>
        {% endblock %}

<br/><br/>
OBS: templates are **HTML**!! (look the extension)

-----

Django - admin (crown jewell)
=============================

What about creating these tasks? enters the admin =]

<br/><br/>
admin.py
<br/><br/>

    !python
        from minhaapp.models import Task
        from django.contrib import admin
        
        class TaskAdmin(admin.ModelAdmin):
            #customizations goes here
            pass
            
        admin.site.register(Task, TaskAdmin)
        
-----

Django - forms
===============

adding a task through a page (using forms)

<br/><br/> 
forms.py: 
<br/><br/>

    !python
        # forms from model
        class TaskForm(forms.ModelForm):
            class Meta:
                model = Task
 
        #creating manually:
        class Task(forms.Model):
            title = forms.TextField('Titulo', max_length=100)
            text = forms.TextField('Texto', max_length=400, required = False
                        widget=forms.Textarea)
           owner = forms.ChoiceField(choices = User.objects.all())

-----

Django - processing forms
==========================

views.py

    !python
        def task_create(request):
            form = TaskForm(request.POST or None)
            if form.is_valid():
                form.save()
            return render_to_response('task_create.html', {'form', form},
                            context_instance = ContextRequest(request))
<br/>
task_create_.html

    !html
        <form>
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="send">
        </form>
  
<br/><br/>
Uffs .... that was hard!! ..... **bazinga**!!

-----

Django - querys
===============

Some simple query operations:

    !python
        # save 
        b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
        b.save()

        # get
        entry = Entry.objects.get(pk=1)
        cheese_blog = Blog.objects.get(name="Cheddar Talk")

        # m2m
        joe = Author.objects.create(name="Joe")
        entry.authors.add(joe)
        
        # get many entrys
        all_entries = Entry.objects.all()
        Entry.objects.order_by('headline')[5:10]
        
        # chaining query-sets objects (not that you should)
        Entry.objects.filter(headline__startswith='What'
            ).exclude(pub_date__gte=datetime.now()
            ).filter(pub_date__gte=datetime(2005, 1, 1))

------

Django - querys
===============

Complex lookups with Q objects:

    !python
        Poll.objects.get( Q(question__startswith='Who'),
            Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))

following relationships backwards:

    !python
        b = Blog.objects.get(id=1)
        b.entry_set.all()

eager loading:

    !python
        e = Entry.objects.get(id=5)
        # Hits the database again to get the related Blog object.
        b = e.blog
        
        e = Entry.objects.select_related().get(id=5)
        # Doesn't hit the database, because e.blog has been prepopulated in the previous query.
        b = e.blog
        
raw (native) sql:

    !python
        Person.objects.raw('SELECT * FROM myapp_person')
        TabelaQualuqer.objects.raw('QUERY REALMENTE LONGA E ASSUSTADORA, AQUI!')


-----

Django - pluggable apps
=======================

* finally, real code reuse!
* do not reinvent the wheel (unless explicitly and objectively necessary)
* almost like playing with legos
* still very customizable
* Unix philosophy (**"Do one thing and do it well"**)
* everything is pure/simple/plain python ... infinite possibilities

some python goodies and other tips
==================================

* pylint, pyflakes, pep8  -> code helpers
* fabric  -> automatize deploy, independent from technology 
* gunicorn + nginx 
* use pip and virtualenv..always..seriously!

-----

Django - auth / profiles
========================

* Full authentication app on django.contrib.auth
* django.contrib.auth.models.User:
    * groups
    * permission
    * roles (staff & admininstrator, used by django-admin app)
* hooks for custom profiles (like the get_profile() method)
* ready-to-use views for commons operations:
    * url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    * url(r'^logout/$','django.contrib.auth.views.logout',{'template_name': 'logout.html'}),
* forms for commons operations: 
    * AuthenticationForm, PasswordChangeForm, PasswordResetForm, UserChangeForm, UserCreationForm

-----

Django - scalability - caches
====================
To setup:

    !python
        CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                'LOCATION': '127.0.0.1:11211',
            }
        }

OBS: Memcached -> ability to share cache over multiple servers. 
You can run Memcached daemons on multiple machines, and the program 
will treat the group of machines as a single cache. Just pass a list in LOCATION 

OBS2: BACKEND for dummy caching (for development purposes): 'django.core.cache.backends.dummy.DummyCache'

To cache all site:

    !python
        MIDDLEWARE_CLASSES = (
            # ...
            'django.middleware.cache.UpdateCacheMiddleware',
            'django.middleware.cache.FetchFromCacheMiddleware',
        )


-----

Django - scalability - caches
=============================

To cache a view:
    
    !python
        from django.views.decorators.cache import cache_page

        @cache_page(60 * 15, cache='my_cache_name')
        def my_view(request):
            ...

Template fragment cache:

    !python
        {% load cache %}
        {% cache 500 sidebar %}
            .. sidebar ..
        {% endcache %}

"low level" cache api:

    !python
        cache.set('my_key', 'my value!', 30)
        cache.get('my_key')
        cache.delete('my_key')



-----

Django - scalability - multi DBs
================================

    !python
        DATABASES = {
            'master': {
                'NAME': 'app_data',
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'USER': 'postgres_user',
                'PASSWORD': 's3krit'
            },
            'slave1': {
                'NAME': 'app_data_slave1',
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'USER': 'postgres_user',
                'PASSWORD': 's3krit'
            }
            'slave2': {
                'NAME': 'app_data_slave2',
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'USER': 'postgres_user',
                'PASSWORD': 's3krit'
            }
        }
        
        DATABASE_ROUTERS = ['path.to.MasterSlaveRouter',]
        
 -----

Django - scalability - multi DBs
================================

    !python
        class MasterSlaveRouter(object):
            def db_for_read(self, model, **hints):
                "Point all read operations to a random slave"
                return random.choice(['slave1','slave2'])

            def db_for_write(self, model, **hints):
                "Point all write operations to the master"
                return 'master'

            def allow_syncdb(self, db, model):
                "Explicitly put all models on all databases."
                return True

<br/>

* That's it =] .... big win!!
* It's possible any kind on customization, for examples:
    * one for master/slave read/write,
    * in the other a DB specific to serve a single app (like users/auth or videos =] )

-----

Django - apps and goodies
=========================
* to name a few:  
<br/>
django-annoying -> one of my favorites (specially for ajax)  
django-registraion  
django-profiles  
django-pagination  
django-video  -> probably usefull for us
django-uploadify  
**django-debug-toolbar**  
**south**  -> migrations !!   
django-paypal  
django-avatar  
**django-haystack** -> indexing   
django-sentry -> interface to interact with your error logs  
django-piston -> helps to create great apis (RESTfull)  
django-social-registration -> google/facebook/twitter/etc  
django-tagging -> easy tags  
django-mailer  
playdoh -> scalability   
django-floppyforms  -> html5 forms  (same api from django.forms)

-----

Questions ?
===========


