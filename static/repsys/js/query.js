// 接收服务器返回来的查询
var q_obj;

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


var waiting = new Vue({
    el: '#waiting',
    data: {
        seen: false
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


var t_obj = {};

function save_query() {
    console.log('请求路径：/savequery');
    t_obj.rid = v_obj.rid;
    t_obj.rname = v_obj.q_name;
    t_obj.rauthor = v_obj.author;
    t_obj.rdept = v_obj.dept;
    t_obj.rcode = v_obj.code;
    t_obj.rcmt = v_obj.comment;
    $.ajax({
        url: '/savequery/',
        type: "POST",
        // contentType: "application/json", //使用这个只能传json字符串，不能传对象
        data: t_obj, //JSON.stringify(t_obj),
        success: function (m) {
            // alert("test......." + data);
            if (m.status) {
                alert("出错啦:" + m.except + "请检查需要保存的查询信息，重试");
            }
            console.log(m)

            popup(200,'test')
            // console.log(data);
            // document.getElementById("data_container").innerHTML = data;
            // console('hi');
        },
        error: function () {
            alert("出错啦，请刷新页面，重试！");
            // console('hi');
        },
    });

}

function del_query() {
    var del_obj = {};
    del_obj.q_id = v_obj.rid;
    $.ajax({
        url: '/del_query/',
        type: 'POST',
        data: del_obj,
        success: function (m) {
            if (m.status) {
                alert("查询删除失败，请重试！")
            }
            else {
                v_obj.author = null;
                v_obj.code = null;
                v_obj.comment = null;
                v_obj.dept = null;
                v_obj.rid = null;
                v_obj.q_name = null;
                alert("查询删除成功！");
            }
        }
    })
}

var rdata;
let elem = document.getElementById('my_viewer');
let side_panel = document.getElementById('side_panel');
let top_panel = document.getElementById('top_panel');
elem.load();

elem.setAttribute("settings", "true");
side_panel.setAttribute("style", "display:flex");
top_panel.setAttribute("style", "display:flex");

function get_data() {
    console.log('请求路径：/exequery');
    waiting.seen = 1;
    let code = v_obj.code;
    // console.log(code);
    $.ajax({
        url: '/exequery/',
        type: "POST",
        // contentType: "application/json",
        data: {"code": code},
        success: function (data) {
            if (data.status) {
                waiting.seen = 0;
                // console.log(data);
                alert("错误：" + data.except +
                    "执行查询时出错：请确认查询无误，重新执行查询！");
            }
            else {
                rdata = JSON.parse(data);
                // console.log(rdata);
                elem.load(rdata);
                waiting.seen = 0;
                // alert("查询执行完毕，数据返回成功！");
                elem.setAttribute('columns-pivots', JSON.stringify(["credit_level"]));
            }
        }
    })

}


function load_data() {
    try {
        elem.load(rdata);
        // alert('数据加载成功，开始你的分析吧！')
    }
    catch (err) {
        alert("错误：" + err + "。" + "请确认查询无误，重新执行查询，加载数据！");
        console.log('加载失败！')
    }
}


function popup(pWidth, content) {
    console.log('hi'+ pWidth + ':' + content);
    $("#msg").remove();
    var html = '<div id="msg" style="position:fixed;top:50%;width:100%;height:30px;line-height:30px;margin-top:-15px;"><p style="background:#000;opacity:0.8;width:' + pWidth + 'px;color:#fff;text-align:center;padding:10px 10px;margin:0 auto;font-size:12px;border-radius:4px;">' + content + '</p></div>'
    $("body").append(html);
    var t = setTimeout(next, 2000);

    function next() {
        $("#msg").remove();

    }
}








