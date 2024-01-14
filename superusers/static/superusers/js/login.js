let form = document.forms[0];
document.getElementById("submit").addEventListener("click", ()=>{
    if(((document.getElementById("username").value).trim()).length == 0 || ((document.getElementById("password").value).trim()).length == 0){
        document.getElementById("invalid").style.display="block";
    }else{
        document.getElementById("invalid").style.display="none";
        form.submit();
    }
});