from wsgiproxy.middleware import WSGIProxyMiddleware


def unproxify(app, *globalconf, **localconf):
    return WSGIProxyMiddleware(app, **localconf)
