from django.urls import path
from django.views.generic import TemplateView

# from .views import CareersView, ContactView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('reports-and-commentary', TemplateView.as_view(template_name="reports-and-commentary.html"), name='reports-and-commentary'),
    path('intelligence-platform', TemplateView.as_view(template_name="intelligence-platform.html"), name='intelligence-platform'),
    path('careers', TemplateView.as_view(template_name="careers.html"), name='careers'),
    path('about-us', TemplateView.as_view(template_name="about-us.html"), name='about-us'),
    path('advisory', TemplateView.as_view(template_name="advisory.html"), name='advisory'),
    path('carbon-credit-prices', TemplateView.as_view(template_name="carbon-credit-prices.html"), name='carbon-credit-prices'),
    path('carbon-credit-integrity', TemplateView.as_view(template_name="carbon-credit-integrity.html"), name='carbon-credit-integrity'),
    path('our-team', TemplateView.as_view(template_name="our-team.html"), name='our-team'),
    path('survey', TemplateView.as_view(template_name="survey.html"), name='survey'),
    path('chinas-voluntary-carbon-market-could-burst-back-into-life', TemplateView.as_view(template_name="chinas-voluntary-carbon-market-could-burst-back-into-life.html"), name='chinas-voluntary-carbon-market-could-burst-back-into-life'),
    path('save-the-date-south-american-carbon-markets-webinar', TemplateView.as_view(template_name="save-the-date-south-american-carbon-markets-webinar.html"), name='save-the-date-south-american-carbon-markets-webinar'),
    path('voluntary-carbon-market-2022-in-review', TemplateView.as_view(template_name="voluntary-carbon-market-2022-in-review.html"), name='voluntary-carbon-market-2022-in-review'),
    path('demystifying-the-use-of-carbon-credits-for-corporate-climate-targets', TemplateView.as_view(template_name="demystifying-the-use-of-carbon-credits-for-corporate-climate-targets.html"), name='demystifying-the-use-of-carbon-credits-for-corporate-climate-targets'),
    path('cop27-in-a-nutshell', TemplateView.as_view(template_name="cop27-in-a-nutshell.html"), name='cop27-in-a-nutshell'),
    path('insurance-carbon-credits', TemplateView.as_view(template_name="insurance-carbon-credits.html"), name='insurance-carbon-credits'),
    path('redd-plus', TemplateView.as_view(template_name ="redd-plus.html"), name='redd-plus'),
    path('easyjet-blog', TemplateView.as_view(template_name ="easyjet-blog.html"), name='easyjet-blog'),
    path('raising-the-bar-will-new-policies-deliver-higher-carbon-credit-quality', TemplateView.as_view(template_name ="raising-the-bar-will-new-policies-deliver-higher-carbon-credit-quality.html"), name='raising-the-bar-will-new-policies-deliver-higher-carbon-credit-quality'),
    path('1h22-review-of-voluntary-carbon-market', TemplateView.as_view(template_name="1h22-review-of-voluntary-carbon-market.html"), name='1h22-review-of-voluntary-carbon-market'),
    path('impact-of-the-voluntary-carbon-market-on-tropical-forest-countries-implications-for-corresponding-adjustments', TemplateView.as_view(template_name="impact-of-the-voluntary-carbon-market-on-tropical-forest-countries-implications-for-corresponding-adjustments.html"), name='impact-of-the-voluntary-carbon-market-on-tropical-forest-countries-implications-for-corresponding-adjustments'),
    path('using-carbon-credits-to-enhance-corporate-climate-action', TemplateView.as_view(template_name="using-carbon-credits-to-enhance-corporate-climate-action.html"), name='using-carbon-credits-to-enhance-corporate-climate-action'),
    path('category/commentary', TemplateView.as_view(template_name="commentry.html"), name='category/commentary'),
    path('category/survey', TemplateView.as_view(template_name="category-survey.html"), name='category/survey'),
    path('category/webinar', TemplateView.as_view(template_name="category-webinar.html"), name='category/webinar'),
    path('overall-summary', TemplateView.as_view(template_name="overall-summary.html"), name='overall-summary'),
    path('tag-carbon-credit-prices', TemplateView.as_view(template_name="tag-carbon-credit-prices.html"), name='tag-carbon-credit-prices'),
    path('tag-carbon-projects-and-transactions', TemplateView.as_view(template_name="tag-carbon-projects-and-transactions.html"), name='tag-carbon-projects-and-transactions'),
    path('tag-carbon-credit-integrity', TemplateView.as_view(template_name="tag-carbon-credit-integrity.html"), name='tag-carbon-credit-integrity'),
    path('reports-and-commentary2', TemplateView.as_view(template_name="reports-and-commentary2.html"), name='reports-and-commentary2'),
    path('cookies-policy', TemplateView.as_view(template_name="cookies-policy.html"), name='cookies-policy'),
    path('terms-of-website-use', TemplateView.as_view(template_name="terms-of-website-use.html"), name='terms-of-website-use'),
    path('acceptable-use-policy', TemplateView.as_view(template_name="acceptable-use-policy.html"), name='acceptable-use-policy'),
    
]   
