function hash33(t) {
    for (var e = 0, i = 0, n = t.length; i < n; ++i)
        e += (e << 5) + t.charCodeAt(i);
    return 2147483647 & e
}

function getToken(p_skey) {
    var str = p_skey || '',
        hash = 5381;
    for (var i = 0, len = str.length; i < len; ++i) {
        hash += (hash << 5) + str.charCodeAt(i);
    }
    return hash & 0x7fffffff;
}

function guid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    }).toUpperCase();
}

function getData(fun){
    function callback(data){
        return data;
    }
    return eval(fun)
}
