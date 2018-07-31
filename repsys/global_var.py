# encoding:utf-8
def get_g_vars(request):
    try:
        userid = request.session['userid']
        username = request.session['username']
        user = {"userid": userid, "username": username}
        return user
    except:
        return {'reason': 'Not Logged In'}
