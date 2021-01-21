var pt = {};
pt.str = {
    no_uin: "你还没有输入帐号！",
    no_pwd: "你还没有输入密码！",
    no_vcode: "你还没有输入验证码！",
    inv_uin: "请输入正确的帐号！",
    inv_vcode: "请输入完整的验证码！",
    qlogin_expire: "你所选择号码对应的QQ已经失效，请检查该号码对应的QQ是否已经被关闭。",
    other_login: "帐号登录",
    h_pt_login: "帐号密码登录",
    otherqq_login: "QQ帐号密码登录",
    onekey_return: "返回扫码登录"
}, pt.ptui = {
    s_url: "https\x3A\x2F\x2Fgraph.qq.com\x2Foauth2.0\x2Flogin_jump",
    proxy_url: "",
    jumpname: encodeURIComponent(""),
    mibao_css: encodeURIComponent(""),
    defaultUin: "",
    lockuin: parseInt("0"),
    href: "https\x3A\x2F\x2Fxui.ptlogin2.qq.com\x2Fcgi-bin\x2Fxlogin\x3Fappid\x3D716027609\x26daid\x3D383\x26style\x3D33\x26theme\x3D2\x26login_text\x3D\x25E6\x258E\x2588\x25E6\x259D\x2583\x25E5\x25B9\x25B6\x25E7\x2599\x25BB\x25E5\x25BD\x2595\x26hide_title_bar\x3D1\x26hide_border\x3D1\x26target\x3Dself\x26s_url\x3Dhttps\x253A\x252F\x252Fgraph.qq.com\x252Foauth2.0\x252Flogin_jump\x26pt_3rd_aid\x3D100497308\x26pt_feedback_link\x3Dhttps\x253A\x252F\x252Fsupport.qq.com\x252Fproducts\x252F77942\x253FcustomInfo\x253D.appid100497308",
    login_sig: "",
    clientip: "",
    serverip: "",
    version: "202101062347",
    ptui_version: encodeURIComponent("21010623"),
    isHttps: 1,
    cssPath: "https://ui.ptlogin2.qq.com/style.ssl/40",
    domain: encodeURIComponent("qq.com"),
    fromStyle: parseInt(""),
    pt_3rd_aid: encodeURIComponent("100497308"),
    appid: encodeURIComponent("716027609"),
    lang: encodeURIComponent("2052"),
    style: encodeURIComponent("40"),
    low_login: encodeURIComponent("0"),
    daid: encodeURIComponent("383"),
    regmaster: encodeURIComponent(""),
    enable_qlogin: "1",
    noAuth: "0",
    target: isNaN(parseInt("0")) ? {_top: 1, _self: 0, _parent: 2}["0"] : parseInt("0"),
    csimc: encodeURIComponent("0"),
    csnum: encodeURIComponent("0"),
    authid: encodeURIComponent("0"),
    auth_mode: encodeURIComponent("0"),
    pt_qzone_sig: "0",
    pt_light: "0",
    pt_vcode_v1: "1",
    pt_ver_md5: "000D64FF6AF2E4247B21E209EB22A1DBCF002087B988CCCCD4B51233",
    gzipEnable: "1"
};



function getPt(){
    return pt;
}
