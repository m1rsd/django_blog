var element = document.getElementById('phone');
var maskOptions = {
    mask: '+{998}(00)000-00-00',
    lazy: false
}
var mask = new IMask(element, maskOptions);

var element2 = document.getElementById('email');
var maskOptions2 = {
    mask: function (value) {
        if (/^[a-z0-9_\.-]+$/.test(value))
            return true;
        if (/^[a-z0-9_\.-]+@$/.test(value))
            return true;
        if (/^[a-z0-9_\.-]+@[a-z0-9-]+$/.test(value))
            return true;
        if (/^[a-z0-9_\.-]+@[a-z0-9-]+\.$/.test(value))
            return true;
        if (/^[a-z0-9_\.-]+@[a-z0-9-]+\.[a-z]{1,4}$/.test(value))
            return true;
        if (/^[a-z0-9_\.-]+@[a-z0-9-]+\.[a-z]{1,4}\.$/.test(value))
            return true;
        if (/^[a-z0-9_\.-]+@[a-z0-9-]+\.[a-z]{1,4}\.[a-z]{1,4}$/.test(value))
            return true;
        return false;
    },
    lazy: false
}
var mask2 = new IMask(element2, maskOptions2);