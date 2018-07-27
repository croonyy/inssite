# encoding:utf-8
def get_g_vars(request):
    try:
        username = request.session['username']
        user = {"username": username}
        return user
    except:
        return {'reason':'Not Logged In'}
