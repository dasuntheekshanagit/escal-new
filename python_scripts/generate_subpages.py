import json
import os
from tqdm import tqdm

def generate_category_pages(categories_filename, pages_path):
    with open(categories_filename, 'r') as f:
        categories = json.load(f)

    for category in tqdm(categories):
        count = categories[category]['count']
        code = categories[category]['code']
        parent = categories[category]['parent']
        template = \
f"""---
layout: default
title: "{category}"
cat_code: {code}
parent_name: {parent.replace('/', '')}
permalink: {parent}/{code}
---

<section class="home-slider owl-carousel">
    <div class="slider-item bread-item" style="background-image: url('{{{{ 'assets/images/img4.jpg' | relative_url }}}}');"
        data-stellar-background-ratio="0.5">
        <div class="overlay"></div>
        <div class="container" data-scrollax-parent="true">
            <div class="row slider-text align-items-end">
                <div class="col-md-7 col-sm-12 ftco-animate mb-5">
                    <p class="breadcrumbs" data-scrollax=" properties: {{ translateY: '70%', opacity: 1.6}}"><span
                            class="mr-2"><a href="{{{{ site.url }}}}{{{{ site.baseurl }}}}">Home</a></span>/ <span><a href="{{{{ site.url }}}}{{{{ site.baseurl }}}}/{{{{ page.parent_name }}}}">{{{{ page.parent_name }}}}</a></span> / <span>{{{{ page.cat_code }}}}</span></p>
                    <h1 class="mb-3 font-weight-bold" data-scrollax=" properties: {{ translateY: '70%', opacity: .9}}">
                        ESCAL Related Projects
                    </h1>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="ftco-section">
    <div class="container">
        <div class="row">
            <div class="col-md-8">
                <div class="row justify-content-center mb-5 pb-3">
                    <div class="col-md-7 heading-section ftco-animate text-center">
                    <h2 class="mb-4">{{{{ page.title }}}}</h2>
                    </div>
                </div>
                <div class="row">
                    {{% assign projects = site.data.projects %}}
                    {{% assign category_projects = site.data.project_categories['{category}'].projects %}}
                    {{% for _project in category_projects %}}
                        {{% assign project = projects[_project] %}}
                        <div class="col-lg-6 ftco-animate">
                            <div class="blog-entry">
                                {{% assign proj_img = project.category.code | prepend: "assets/images/thumb_" | append: ".jpg" %}}
                                <a href="{{{{ project.page_url }}}}" class="block-20"
                                    style="background-image: url('{{{{ proj_img | relative_url }}}}'); border-radius: 10px;">
                                </a>
                                <div class="text d-flex py-4">
                                    <div class="">
                                        <h3 class="heading"><a href="{{{{ project.page_url }}}}">{{{{ project.title }}}}</a></h3>
                                        {{% assign size = project.team.size %}}
                                        {{% if size > 0 %}}
                                            <div class='d-flex flex-wrap' style="max-width: 350px;">
                                                <span class="icon-person" style="line-height: 1.8;">{{{{ size }}}}</span>
                                                {{% for member in project.team %}}
                                                    {{% assign names = member.name | split: ' ' %}}
                                                    <a href="#" class="px-2">{{{{ names[0] }}}}</a>
                                                {{% endfor %}}
                                            </div>
                                        {{% endif %}}
                                        <p>{{{{ project.description | truncatewords: 30 }}}}</p>
                                        <p><a href="{{{{ project.project_url }}}}" class="btn btn-primary btn-outline-primary">Read
                                                more</a></p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    {{% endfor %}}
                </div>
                <div class="row mt-5">
                    <div class="col">
                        <div class="block-27">
                            <ul>
                                <li><a href="#">&lt;</a></li>
                                <li class="active"><span>1</span></li>
                                <li><a href="#">2</a></li>
                                <li><a href="#">3</a></li>
                                <li><a href="#">4</a></li>
                                <li><a href="#">5</a></li>
                                <li><a href="#">&gt;</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4 sidebar ftco-animate">
                <div class="sidebar-box">
                    <form action="#" class="search-form">
                        <div class="form-group">
                            <span class="icon fa fa-search"></span>
                            <input type="text" class="form-control" placeholder="Type a keyword and hit enter">
                        </div>
                    </form>
                </div>
                <div class="sidebar-box ftco-animate">
                    <div class="categories">
                        <h3>Categories</h3>
                        {{% assign categories = site.data.project_categories | sort %}}
                        {{% for category in categories %}}
                            {{% if category[1].code == page.cat_code %}}
                                {{% continue %}}
                            {{% endif %}}
                            <li><a href="{{{{ site.url }}}}{{{{ site.baseurl }}}}{{{{ category[1].parent }}}}/{{{{ category[1].code }}}}">{{{{ category[0] | truncate:35 }}}} <span>({{{{ category[1].count }}}})</span></a></li>
                        {{% endfor %}}
                    </div>
                </div>

                <div class="sidebar-box ftco-animate">
                    <h3>Recent Projects</h3>
                    <div class="block-21 mb-4 d-flex">
                        <a class="blog-img mr-4" style="background-image: url('{{{{ '/assets/images/img1.jpg' | relative_url }}}}'); border-radius: 5px;"></a>
                        <div class="text">
                            <h3 class="heading"><a href="#">Even the all-powerful Pointing has no control about the
                                    blind texts</a></h3>
                            <div class="meta">
                                <div><a href="#"><span class="icon-calendar"></span> July 12, 2018</a></div>
                                <div><a href="#"><span class="icon-person"></span> Admin</a></div>
                                <div><a href="#"><span class="icon-chat"></span> 19</a></div>
                            </div>
                        </div>
                    </div>
                    <div class="block-21 mb-4 d-flex">
                        <a class="blog-img mr-4" style="background-image: url('{{{{ '/assets/images/img2.jpg' | relative_url }}}}'); border-radius: 5px;"></a>
                        <div class="text">
                            <h3 class="heading"><a href="#">Even the all-powerful Pointing has no control about the
                                    blind texts</a></h3>
                            <div class="meta">
                                <div><a href="#"><span class="icon-calendar"></span> July 12, 2018</a></div>
                                <div><a href="#"><span class="icon-person"></span> Admin</a></div>
                                <div><a href="#"><span class="icon-chat"></span> 19</a></div>
                            </div>
                        </div>
                    </div>
                    <div class="block-21 mb-4 d-flex">
                        <a class="blog-img mr-4" style="background-image: url('{{{{ '/assets/images/img3.jpg' | relative_url }}}}'); border-radius: 5px;"></a>
                        <div class="text">
                            <h3 class="heading"><a href="#">Even the all-powerful Pointing has no control about the
                                    blind texts</a></h3>
                            <div class="meta">
                                <div><a href="#"><span class="icon-calendar"></span> July 12, 2018</a></div>
                                <div><a href="#"><span class="icon-person"></span> Admin</a></div>
                                <div><a href="#"><span class="icon-chat"></span> 19</a></div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="sidebar-box ftco-animate">
                    <h3>Tag Cloud</h3>
                    <div class="tagcloud">
                        <a href="#" class="tag-cloud-link">Embedded</a>
                        <a href="#" class="tag-cloud-link">Embedded-Systems</a>
                        <a href="#" class="tag-cloud-link">Biomed</a>
                        <a href="#" class="tag-cloud-link">GPU-Computing</a>
                        <a href="#" class="tag-cloud-link">Bio-Medical</a>
                        <a href="#" class="tag-cloud-link">3YP</a>
                        <a href="#" class="tag-cloud-link">Research-Project</a>
                        <a href="#" class="tag-cloud-link">CUDA</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
        """
        
        with open(f'{pages_path}/{code}.html', 'w') as f:
            f.write(template)

def remove_category_pages(pages_path):
    for f in os.listdir(pages_path):
        if f == 'index.html':
            continue
        if f.endswith('.html'):
            os.remove(os.path.join(pages_path, f))

if __name__ == '__main__':
    generate_category_pages('../_data/project_categories.json', '../pages/projects')
    # remove_category_pages('../pages/projects')