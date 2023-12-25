# # def my_middleware(get_response):
# #     print("Middleware has initialized")
# #
# #     def fun_middleware(request):
# #         print("This is before view calling")
# #         resource = get_response(request)
# #         print("This is after view calling")
# #         return resource
# #     return fun_middleware
#
#
# # ex with class based middleware
# from django.http import HttpResponse
#
#
# class FirstMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         print("First middleware before view")
#         response = HttpResponse("<h3>Response come from first middleware</h3>")
#         print("First middleware after view")
#         return response
#
#
# class SecondMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         print("Second middleware before view")
#         response = HttpResponse("<h3>Response come from second middleware</h3>")
#         print("Second middleware after view")
#         return response
#
#
# class ThirdMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         print("Third middleware before view")
#         response = HttpResponse("<h3>Response come from third middleware</h3>")
#         print("Third middleware after view")
#         return response

from django.http import HttpResponse


# class SiteUnderConstructionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         return HttpResponse("<h2>Currently site is under construction please visit after sometime</h2>")


class ErrorMessageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        return self.get_response(request)

    def process_exception(self,request,exception):
        return HttpResponse("<h3>Currently we are facing some technical issues</h3>")
