$.ajaxSetup({

});

$(document).ready(function(){
    var url = document.URL
    var domain = url.split('/')[4]
    console.log(domain)
    $.ajax({
        type: 'POST',
        url : '/enrichment/ajax_domain/',
        data : {'domain' : domain},
        success:function(response){
            console.log(response)
        },
        error :function(){
            alert('Something error');
        }
    })
})