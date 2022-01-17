const x64617465 = new Date();
x79 = x64617465.getFullYear();
x6d = x64617465.getMonth() + 1;
x64 = x64617465.getDate();
key = "0x" + (x79 * x6d * x64 * (862 + 49)).toString(4 * 4)
document.getElementById("key").value = key

function copy() {
    var cp = document.getElementById('key').value
    const el = document.createElement('textarea');
    el.value = cp;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
}

var toastTrigger = document.getElementById('liveToastBtn')
var toastLiveExample = document.getElementById('liveToast')
if (toastTrigger) {
    toastTrigger.addEventListener('click', function () {
        var toast = new bootstrap.Toast(toastLiveExample)
        toast.show()
    })
}