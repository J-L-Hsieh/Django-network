$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function(){

    $('#submit_mode1').click(function(){
        console.log($('#search_mode1').serialize())

        $.ajax({
            url: 'ajax_mode1/',
            data: $('#search_mode1').serialize(),
            success: function(response){
                var data = response
                // console.log(typeof(data))
                // console.log(response)
                // console.log(response.table2_data.length)
                search = response.search
                var len = data.table2_data.length

                if (response.wormbase_id == 'error'){
                    alert("Can't find the unique Wormbase ID")
                }else{
                    $("#Answer1").html('<table id="mode1_table1" class="display" style="width:100%"></table>');
                    $('#mode1_table1').DataTable({
                        'data' : [data],
                        'columns' : [
                            {data : 'wormbase_id' ,title:'Wormbase ID'},
                            {data : 'Sequence', title: 'Sequence'},
                            {data : 'gene_name' ,title:'Gene Name'},
                            {data : 'other_name' ,title:'Other Name'},
                        ],
                        "createdRow": function( row, data,dataIndex) {
                            if ( data.wormbase_id == search ) {
                                $(row).addClass('rowyellow');
                            }
                        },
                    })
                    $("#Answer2").html('<table id="mode1_table2" class="display" style="width:100%"></table>');
                    $('#mode1_table2').DataTable({
                        'data' : data.table2_data,
                        'columns' : [
                            {data : 'transcript' ,title:'transcript ID',
                            "render": function(data, type, row, meta){
                                data = '<a href ="/detail/' + data + '">' + data + '</a>';
                                // data = `<a herf= "/detail/${data}">${data}</a>`
                                return data;
                            }},
                            {data : 'gene_type', title: 'gene_type'},
                            {data : 'transcript' ,title:'PirScan',
                                'render': function (data, type, row, meta) {
                                    data = `<a href ="/result/?id=${data}">tool</a>`;

                                    return data;
                                }
                            },
                        ],
                        "createdRow": function( row, data, dataIndex) {
                                if ( data.transcript == search ) {
                                $(row).addClass('rowyellow');
                                }
                        },
                    })
                }
            },
            error: function(){
                alert('Something error');
            },
        })
    });
});
