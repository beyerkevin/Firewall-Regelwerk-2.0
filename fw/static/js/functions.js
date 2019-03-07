
$(document).ready(function(){
    $("#btnSidebar").click(function(e){
        e.preventDefault();
        $("#wrapper").toggleClass("menuDisplayed");
    });
      
 });
/*
 $(document).ready(function(){
     
    $("#content").load("static/fw/index.html");

});

$(document).ready(function(){

    $("#sidebar-wrapper").load("static/fw/sidebar.html");
});

*/

$(document).ready(function(){
    $("#content").load("fw/templates/fw/index.html", function(){
        alert("Test");
    });
});