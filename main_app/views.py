from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class Brand:
    def __init__(self, name, image):
        self.name=name
        self.image=image

class Polish:
    def __init__(self, name, image, brand):
        self.name = name
        self.image = image
        self.brand = brand

brands = [
    Brand("OPI", "https://findvectorlogo.com/wp-content/uploads/2022/02/opi-products-inc-vector-logo-2022.png"),
    Brand("Essie", "https://lotusnaildenmark.files.wordpress.com/2017/03/essie-logo.jpeg"),
    Brand("China Glaze", "https://phyrra.net/wp-content/uploads/2019/01/china-glaze.jpg"),
    Brand("Zoya", "https://uspto.report/TM/90736063/mark.png"),
    ]

polishes = [
    Polish("Left Your Texts on Red", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYLDdgjRAaeoHC-cSyzJja2WnX0K88oSjMAM8o19mmkOwo5c4D8M6TUkVTOHPDSF2U27RbUOpGx5Geh3IMOUOofgfqhB5fs33gnKHBz59OvzFqvgK2RbbzpASNUH2h17BKHpBkjsEqFRce5nsjXZl4BU_K9rfKuVzX6gu4GNGA7B9k8Qt8mvLsx8hykA/s1600/opi-spring-2023-me-myself-and-opi-collection-review-swatches-left-your-texts-on-red.png", "OPI"),
    Polish("Silicon Valley Girl", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-bGSLEpfDiqLOMIN5sE79dbGyqNCSjKQA_MLRhZz5jFluzdW2F4lzSnaRVft8AT5vWYywN8SbetgiUTXGuWGVRPMwdYA7wYC-ZDpkuvk-FJX7wVDmRVsCUtnJCzGry8I83Od6X6g9k05ZmMNxMf7bTy2r0BKdREc4GJRtvdykwReOI0sxA8m_RSYBUg/s1600/opi-spring-2023-me-myself-and-opi-collection-review-swatches-silicon-valley-girl.png", "OPI"),
    Polish("Blinded by the Ring", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEE0CATC89XM-pHPJxVObaq9XbQYyJZnoiXX_XYXEhsgNjS4Pk4jOuELe-Q5edlFcXDRTvK2Lub3cncJs3_qhJIJ8Ibx1Mxi9skPSbrD_4PC1FW9nbiX5QaEsIhhWtSRGgjUfNwISoyRWQZbAkTWKpC9qo-10CutovjbaA1DTkyIFGEldakUgtDH_znA/s1600/opi-spring-2023-me-myself-and-opi-collection-review-swatches-blinded-by-the-ring-light.png", "OPI"),
    Polish("NFTease Me", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjg8yQ4qXdEMWqNTveWJiOa9gnErVf8kxy-xu7qB4QCTxJRerVTAZr0XFCStSp2TSuXINSxxuhVYcGbmtkiHk08g-QDKQ7OxdcgOCogg8qhzm4jxTH5ujTQXggEaMzQXG7_Xyqd4ypPLnLhZRWkzyeRGEORTPhzkAxS3qAMpdBd72ySK-qjyGB6kafaQ/s1600/opi-spring-2023-me-myself-and-opi-collection-review-swatches-nftease-me.png", "OPI"),
    Polish("Sold My Crypto", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCWEWmn0Thdr3SzipnkTfcufyhMETTx9BL-l4EadhAcBToJrwT1J5qVh6wxSVcWOQWDqN0zYk5xBlh7uAF9ZfVfJJXfUvv35jqoQhqqx1xlRdU9KM3bziRUvc1UBF4__uJw5Zi2I8wtWjviuLDerl3L89qvVRm_POEGS7BT-Fir9rV-YFAlsOAHhrIFw/s1600/opi-spring-2023-me-myself-and-opi-collection-review-swatches-i-sold-my-crypto.png", "OPI"),
    Polish("Sprint Break the Internet", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgROsKjHu6bssZlvzl19KrZqdwDNttxFA9SZF4u-zmVVfxAJBTZpl7KhrliAu_zBdTBNXCzAgeCx9AQPHF5cOgcoi80ucx1XJJZ1FHEbonoVj4S_GtLOwRopIjWEdX626j39Uiy0SYFfRaEmiPI_FedtSWnZm9V4rvoapxr6JROAh43-NIFZiF8qdU2Kw/s1600/opi-spring-2023-me-myself-and-opi-collection-review-swatches-spring-break-the-internet.png", "OPI"),
    Polish("Pink in Bio", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiirYBMh6GgUhi_ZFw5gtux2TXqlrJ1eAk0_mRVk3NcPGuI3ZfrSRR07moywXu2bJdVM0eFnq6PSvyGkHmxBU77TOtmW6lUHcdwsC_91tOrH71jep8KNMmdhRgFdhvUGNUXFShKFhRo4YgYyZn-Kxj2BMFTnFhaTPhpE6-haVk6Mw7D646mrzdRRfjBJQ/s1600/opi-spring-2023-me-myself-and-opi-collection-review-swatches-pink-in-the-bio.png", "OPI"),
    Polish("Clear Your Cash", "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghtswo5upUUamoU2SFIGgfP3FTdpSGRi_hQ4kWi5az8IJcbTYv_SVP_2VDiouKHgKB9gjBLhT69qnkudNXy9hufH9OFkxWBZg35_j8fP2_Xc-PZ2KHWbvAj2o180ZtxdA3LSzT4WhLrR3OFitWkjPUrfiyfSmspo20lSQeyxfgKSSCJMX57ynSEvjLMw/s1600/opi-spring-2023-me-myself-and-opi-collection-review-swatches-clear-your-cash.png", "OPI"),
    Polish("Feeling Wellies", "https://1.bp.blogspot.com/-QzH4PkSmIlE/XpsXth0cITI/AAAAAAAAipg/kU01xnFk78EgwRFriJLRK4C2vZ9WEKFGgCLcBGAsYHQ/s1600/essie-spring-2020-feeling-wellies-review-swatches.jpg", "Essie"),
    Polish("Can Dew Attitude", "https://1.bp.blogspot.com/-8jfh7-7fhks/XpsXud5uygI/AAAAAAAAipo/BgjeTY827CUiE_1Q1KupdDnAtGTvAe3PwCLcBGAsYHQ/s1600/essie-spring-2020-can-dew-attitude-review-swatches.jpg", "Essie"),
    Polish("Spring in Your Step", "https://1.bp.blogspot.com/-_Zi7F1rdXxM/XpsXypZ15BI/AAAAAAAAip4/we2h8nlIUKQ8gBQgQ_zflnYMWNC6n9yKgCLcBGAsYHQ/s1600/essie-spring-2020-spring-in-your-step-review-swatches.jpg", "Essie"),
    Polish("Make a Splash", "https://1.bp.blogspot.com/-rRcqK9nyu0Y/XpsXxkxeNQI/AAAAAAAAip0/4UTucrEWERES98VwFBzOD23AdS5rIiyKQCLcBGAsYHQ/s1600/essie-spring-2020-make-a-splash-review-swatches.jpg", "Essie"),
    Polish("Sparrow", "https://www.cosmeticsanctuary.com/wp-content/uploads/2022/11/Zoya-Sparrow-1.jpg", "Zoya"),
    Polish("Tamiah", "https://www.cosmeticsanctuary.com/wp-content/uploads/2022/11/Zoya-Tamiah-1.jpg", "Zoya"),
    Polish("Malana", "https://www.cosmeticsanctuary.com/wp-content/uploads/2022/11/Zoya-Malana-1.jpg", "Zoya"),
    Polish("Clarice", "https://www.cosmeticsanctuary.com/wp-content/uploads/2022/11/Zoya-Clarice-1.jpg", "Zoya"),
    Polish("Metora", "https://www.cosmeticsanctuary.com/wp-content/uploads/2022/11/Zoya-Metora-1.jpg", "Zoya"),
    Polish("Rosalind", "https://www.cosmeticsanctuary.com/wp-content/uploads/2022/11/Zoya-Rosalind-1.jpg", "Zoya"),
]

# Create your views here.

class Home(TemplateView):
    template_name='home.html'

class About(TemplateView):
    template_name='about.html'

class BrandList(TemplateView):
    template_name = 'brand_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = brands
        return context

class PolishList(TemplateView):
    template_name = 'polish_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['polishes'] = polishes
        return context
