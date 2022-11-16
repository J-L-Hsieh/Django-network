$.ajaxSetup({
    // headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function() {
    $('#submit_input').click(function(){
        var str = $('#input').serialize();
        var type = str.split('&')[1];
        console.log(type)

        if (type == 'type=none'){
            type = ''
        }else{
            type = '('+type.substring(5)+')';
        }
        console.log($('#input').serialize())
        $.ajax({
            url: 'ajax_enrichment/',
            data: $('#input').serialize(),

            success: function(response){
                console.log(response.result)
                $('#Answer1').html('<table id="result_table" class="display" style="width:100%"></table>');
                $('#result_table').DataTable({
                    'data' : response.result,
                    'columns' : [
                        {data : 'Domain Name' ,title:'Domain Name'},
                        {data : 'Expext Ratio', title: 'Expext Ratio'},
                        {data : 'Observed Ratio', title: 'Observed Ratio'},
                        {data : 'P-value', title: `P-value${type}`},
                        {data : 'Domain Name' , title:'detail',
                        render: function(data, type, row, meta){
                                data = '<button class = "detail" id = "'+ meta.row+ '">Detail</button>';
                            return data;
                        }
                        },

                    ]
                });
                $('#result_table').on('click','.detail',function(){
                    var detail_num = $(this)[0].attributes.id.value
                    var data_detail = JSON.parse(response.all_table[detail_num])
                    $('#Answer2').html('<table id="detail_table" class="display" style="width:100%"></table>');
                    $('#detail_table').DataTable({
                        'data' : data_detail,
                        'columns' : [
                            {data : 'all' , title : 'Systematic Name'},
                            {data : 'input' , title : 'Input',
                            render: function(data){
                                if (data ==='true'){
                                    return '<div>&#9989</div>'
                                }else{
                                    return '<div>&#10060</div>'
                                }
                            }
                            },
                            {data : 'domain' ,title : 'Domain',
                            render: function(data){
                                if (data ==='true'){
                                    return '<div>&#9989</div>'
                                }else{
                                    return '<div>&#10060</div>'
                                }
                            }
                            },
                        ]
                    });
                });
            },
            error: function(){
                alert('Something error');
            },
        });
    });
});