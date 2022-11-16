$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function(){

    $('#pirscan_input').click(function(){
        $.ajax({
            url: '/pirscan/search/',
            data: $('#pirscan').serialize(),
            success: function(response){
                var data = response.result
                $("#pirscan_result").html('<table id="pirscan_table" class="display" style="width:100%"></table>');
                $('#pirscan_table').DataTable({
                    'data' : data,
                    'columns' : [
                        {data : 'piRNA' ,title : 'piRNA'},
                        {data : 'target',title : 'targeted region in '+response.name},
                        {data : 'score', title: 'piRNA targeting score'},
                        {data : 'position',title:'position in piRNA'},
                        {data : 'pairing' ,title:' paring(top: '+response.name+',bottom : piRNA)'},
                    ]
                });
            },
            error: function(){
                alert('Something error');
            },
        });
    });
});
