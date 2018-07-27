// 设置数据源的几种方式


var data;
let elem = document.getElementById('my_viewer');
elem.load([{x: 1, y: 'a'}, {x: 2, y: 'b'}]);

// $('#load_engine').click(function () {
//     elem.load([{x: 1, y: 'a'}, {x: 2, y: 'b'}]);
//     console.log('load')
// });


//
// $('#load_data').click(function () {
//     new Promise(function (ok, nok) {
//         $.getJSON('/ajax_list/', function (ret) {
//             //    返回值ret在这里是一个列表
//             data = JSON.parse(ret);
//
//             // console.log(data);
//             console.log(typeof(data));
//         });
//         ok(1);
//     }).then(function (value) {
//         console.log(value);
//         elem.load(data);
//         // elem.setAttribute('columns', JSON.stringify(["y"]));
//         // elem.setAttribute('sort', JSON.stringify([["x","asc"]]));
//     });
// });
//
//
// function test2() {
//
//     elem.load(data)
//     console.log('load')
// }


// let data = [
//     {'你': 1, '2': 'a'},
//     {'你': 2, '2': 'b'}
// ];
// let data = "A,B,C\n10,a,3\n2,b,4\n5,b,7\n4,c,6";

// elem.setAttribute('columns', ["y"]);
// elem.setAttribute('columns', []);
// let table = elem.worker.table(data);
// console.log(table);

//
// new Promise(function (ok, nok) {
//     elem.update(data);
//     console.log('data_loading');
//     ok(123)
// }).then(function (value) {
//     console.log('loaded');
//     // elem.setAttribute('columns', JSON.stringify(["y"]));
//     // elem.setAttribute('sort', JSON.stringify([["x","asc"]]));
// });

// columns="["y"]"
// elem.setAttribute('aggregates',{"y":"distinct count","x":"sum","z":"sum"});


// let my_viewer = document.getElementById('my_viewer');
// my_viewer.load([{x: 1, y: 'a'},{x: 2, y: 'b'}]);
// function test() {
//     // let a = document.getElementById('my_viewer');
//     // c = a.getAttribute('columns');
//     // d = a.getAttribute('aggregates');
//     // sort = a.getAttribute('sort');
//     // console.log(typeof(c));
//     // console.log(typeof(d));
//     // console.log(typeof(sort));
//     // console.log(c, d, sort);
//     // let data_re =[
//     //     {A: 1, B: 'a'},
//     //     {A: 2, B: 'b'}
//     // ];
//     my_viewer = document.getElementById('my_viewer');
//     let table = my_viewer.worker.table([{a: 1, b: 2}]);
//     my_viewer.load(table);
//     // console.log(data_re)
//     console.log(my_viewer.getAttribute('columns'))
// };

