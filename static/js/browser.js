$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function(){
    $('.myform').on('submit', function(e){
        e.preventDefault();
        var checkboxvalue =  [];
        $("input[type=checkbox]:checked").each(function(i){
            checkboxvalue.push($(this).val());
            console.log(checkboxvalue)
        });
        $.ajax({
            url: '/browser/ajax_browser/',
            data: {'checkboxvalue': checkboxvalue},
            success: function(data){
                console.log(data.table)
                $('#type1').html('<table id="browser_table" class="display" style="width:100%"></table>');
                $('#browser_table').DataTable({
                    'data' : data.table,
                    'columns' : [
                        {data : 'Wormbase ID' ,title:'Wormbase ID'},
                        {data : 'transcript', title: 'transcript',
                        "render": function(data, type, row, meta){
                            data = '<a href ="/detail/' + data + '">' + data + '</a>';
                            return data;
                        }},
                        {data : 'type', title: 'Type'},
                    ]
                });
            },
            error: function(){
                alert('Something error');
            },
        });
    });
});
