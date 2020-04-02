function changeselect(){
    var bs = document.getElementById('bs');
    var ss = document.getElementById('ss');
    var qs = document.getElementById('qs');
    var ele = document.getElementById('element');
    if(bs.selected == true){
        ele.disabled = false;
    }else{
        ele.disabled = true;
    }
}
