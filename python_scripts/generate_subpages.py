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
                <div class="row" id='projects-layout' data-current-page='1'>
                    {{% assign projects = site.data.projects %}}
                    {{% assign category_projects = site.data.project_categories['{category}'].projects %}}
                    {{% for _project in category_projects %}}
                        {{% assign project = projects[_project] %}}
                        <div class="col-lg-6 ftco-animate project-card">
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
                                                    {{% assign names = member[1].name | split: ' ' %}}
                                                    <a href="#" class="px-2">{{{{ names[0] }}}}</a>
                                                {{% endfor %}}
                                            </div>
                                        {{% endif %}}
                                        <span class="icon-calendar" style="line-height: 1.8;"> {{{{ project.updated_at | date: '%b %d, %Y' }}}}</span>
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
                        <div class="block-27 d-flex justify-content-center">
                            <ul>
                                {{% assign pages = category_projects.size | divided_by: 10.0 | ceil %}}
                                <li><a id='prev-button' href="#">&lt;</a></li>
                                <li><a class="page-button" data-page='1' href="#">1</a></li>
                                {{% for i in (2..pages) %}}
                                    <li><a class="page-button" data-page='{{{{ i }}}}' href="#">{{{{ i }}}}</a></li>
                                {{% endfor %}}
                                <li><a id='next-button' href="#">&gt;</a></li>
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
                        {{% for category in site.data.project_categories %}}
                            {{% if category[1].code == page.cat_code %}}
                                {{% continue %}}
                            {{% endif %}}
                            <li><a href="{{{{ site.url }}}}{{{{ site.baseurl }}}}{{{{ category[1].parent }}}}/{{{{ category[1].code }}}}">{{{{ category[0] | truncate:35 }}}} <span>({{{{ category[1].count }}}})</span></a></li>
                        {{% endfor %}}
                    </div>
                </div>

                <div class="sidebar-box ftco-animate">
                    <h3>Recent Projects</h3>
                    {{% assign first_proj = nil %}}
                    {{% assign first_recent = '0000-0-0T00:00:00Z' %}}
                    {{% for _project in category_projects %}}
                        {{% assign project = projects[_project] %}}
                        {{% if project.updated_at > first_recent %}}
                            {{% assign first_recent = project.updated_at %}}
                            {{% assign first_proj = project %}}
                        {{% endif %}}
                    {{% endfor %}}
                    {{% assign proj_img = first_proj.category.code | prepend: "assets/images/thumb_" | append: ".jpg" %}}
                    {{% if first_proj %}}
                        <div class="block-21 mb-4 d-flex">
                            <a class="blog-img mr-4" style="background-image: url('{{{{ proj_img | relative_url }}}}'); border-radius: 5px;"></a>
                            <div class="text">
                                <h3 class="heading"><a href="{{{{ first_proj.project_url }}}}">{{{{ first_proj.title }}}}</a></h3>
                                <div class="meta">
                                    <div><span class="icon-calendar"></span> {{{{ first_proj.updated_at | date: '%B %d, %Y' }}}}</div>
                                    {{% if first_proj.team.size > 0 %}}
                                        <div><span class="icon-person"></span> {{{{first_proj.team.size}}}}</div>
                                    {{% endif %}}
                                    <div><span class="icon-star"></span> {{{{first_proj.stars}}}}</div>
                                </div>
                            </div>
                        </div>
                    {{% endif %}}

                    {{% assign second_proj = nil %}}
                    {{% assign second_recent = '0000-0-0T00:00:00Z' %}}
                    {{% if first_proj %}}
                        {{% for _project in category_projects %}}
                            {{% assign project = projects[_project] %}}
                            {{% if first_recent > project.updated_at > second_recent %}}
                                {{% assign second_recent = project.updated_at %}}
                                {{% assign second_proj = project %}}
                            {{% endif %}}
                        {{% endfor %}}
                        {{% assign proj_img = second_proj.category.code | prepend: "assets/images/thumb_" | append: ".jpg" %}}
                    {{% endif %}}

                    {{% assign third_proj = nil %}}
                    {{% assign third_recent = '0000-0-0T00:00:00Z' %}}
                    {{% if second_proj %}}
                        <div class="block-21 mb-4 d-flex">
                            <a class="blog-img mr-4" style="background-image: url('{{{{ proj_img | relative_url }}}}'); border-radius: 5px;"></a>
                            <div class="text">
                                <h3 class="heading"><a href="{{{{ second_proj.project_url }}}}">{{{{ second_proj.title }}}}</a></h3>
                                <div class="meta">
                                    <div><span class="icon-calendar"></span> {{{{ second_proj.updated_at | date: '%B %d, %Y' }}}}</div>
                                    {{% if second_proj.team.size > 0 %}}
                                        <div><span class="icon-person"></span> {{{{second_proj.team.size}}}}</div>
                                    {{% endif %}}
                                    <div><span class="icon-star"></span> {{{{second_proj.stars}}}}</div>
                                </div>
                            </div>
                        </div>
                        {{% for _project in category_projects %}}
                            {{% assign project = projects[_project] %}}
                            {{% if second_recent > project.updated_at > third_recent %}}
                                {{% assign third_recent = project.updated_at %}}
                                {{% assign third_proj = project %}}
                            {{% endif %}}
                        {{% endfor %}}
                        {{% assign proj_img = third_proj.category.code | prepend: "assets/images/thumb_" | append: ".jpg" %}}
                    {{% endif %}}

                    {{% if third_proj %}}
                        <div class="block-21 mb-4 d-flex">
                            <a class="blog-img mr-4" style="background-image: url('{{{{ proj_img | relative_url }}}}'); border-radius: 5px;"></a>
                            <div class="text">
                                <h3 class="heading"><a href="{{{{ third_proj.project_url }}}}">{{{{ third_proj.title }}}}</a></h3>
                                <div class="meta">
                                    <div><span class="icon-calendar"></span> {{{{ third_proj.updated_at | date: '%B %d, %Y' }}}}</div>
                                    {{% if third_proj.team.size > 0 %}}
                                        <div><span class="icon-person"></span> {{{{third_proj.team.size}}}}</div>
                                    {{% endif %}}
                                    <div><span class="icon-star"></span> {{{{third_proj.stars}}}}</div>
                                </div>
                            </div>
                        </div>
                    {{% endif %}}
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

                <div class="sidebar-box ftco-animate">
                    <span>Last Updated: {{{{ site.time | date: '%B %d, %Y' }}}}</span>
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