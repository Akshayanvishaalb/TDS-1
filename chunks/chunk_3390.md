### Post 326
**Post URL**: /t/tds-official-project1-discrepencies/171141/326
- **ID**: 616077
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-06T13:00:28.513Z
- **Reply To**: Post 325 (Yashvardhan, 23f2004644)
- **Content**:  
  You have to replicate this test environment for testing.
<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
git clone &lt;your repo url&gt; 
cd &lt;your repo directory&gt; 
docker build -t &lt;your image name&gt; 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 &lt;your image name&gt; 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=&lt;any email&gt; --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was  tested. 
You have to provide a token from your environment for testing. 
The…
  </blockquote>
</aside>

Please replicate this first. We also run it on a linux server.
Kind regards
- **Reactions**: heart (1)
- **Post Number**: 326

