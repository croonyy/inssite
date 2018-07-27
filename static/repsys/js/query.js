// 接受服务器返回来的查询
var q_obj;

var t_obj;

// vue app
var v_obj = new Vue({
    el: '#app',
    data: {
        rid: null,
        q_name: null,
        author: null,
        dept: null,
        code: null,
        comment: null
    }
});


function get_query(id) {
    // alert("get_query");
    // var url='/test-'+id
    console.log('请求路径：/getquery-' + id);
    $.ajax({
        url: '/getquery-' + id,
        type: "GET",
        success: function (ret) {
            // alert("test......." + data);
            console.log(ret);
            q_obj = ret;
            v_obj.rid = q_obj.rid;
            v_obj.q_name = q_obj.rname;
            v_obj.author = q_obj.rauthor;
            v_obj.dept = q_obj.rdept;
            v_obj.code = q_obj.rcode;
            v_obj.comment = q_obj.rcmt;
            // console.log(q_obj.q_name);
        },
        error: function () {
            alert("出错啦，请刷新页面，重试");
            // console('hi');
        },
    });
}

function ref_obg() {
    t_obj.rid = v_obj.rid;
    t_obj.rname = v_obj.q_name;
    t_obj.rauthor = v_obj.author;
    t_obj.rdept = v_obj.dept;
    t_obj.rcode = v_obj.code;
    t_obj.rcmt = v_obj.comment;
    return t_obj
}


function save_query(ref_obg) {
    console.log('请求路径：/savequery');
    $.ajax({
        url: '/savequery/',
        type: "post",
        contentType: "application/json",
        data: JSON.stringify(t_obj),
        success: function (m) {
            // alert("test......." + data);
            console.log(m)
            // console.log(data);
            // document.getElementById("data_container").innerHTML = data;
            // console('hi');
        },
        error: function () {
            alert("出错啦，请刷新页面，重试");
            // console('hi');
        },
    });

}






