"""

"""


class InjectOwnerIntoContextMiddleware(object):
    """
    Marsh X-Enteprise-ID Header into the context.
    """
    def process_request(self, req, resp):
        enterprise_id = req.headers.get('X-ENTERPRISE-ID', 0)
        req.context['Enterprise-Id'] = enterprise_id
