$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});
$(document).ready(function(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const row_name = urlParams.get('id')
    const table_name = urlParams.get('name')
    $('#queried').html(`<p>Queried ${table_name} Term : ${row_name}`)
    $('#associated_title').html(`<p>Associated Term with the Queried ${table_name} Term `)

    console.log(table_name)
    console.log(row_name)

    $.ajax({
        url : '/yeast/ajax_associated/',
        data : {'table_name' : table_name,'row_name':row_name},
        success:function(response){
            $('#Answer1').html(response.associated_table);
            $('#associated_table').DataTable();
            column_order = response.all_tables.column_order
            var add_html = ''
            for (i=0 ;i< column_order.length;i++){
                add_html = add_html+`<div id=${column_order[i]}></div>`
            }
            $('#Answer2').html(add_html)
            for (i=0 ;i< column_order.length;i++){
                $(`#${column_order[i]}`).html(response.all_tables[column_order[i]])
                $(`#${column_order[i]}_table`).DataTable({
                    'columnDefs':[
                        {   'targets':-1,
                            'data':null,
                            render:function(row){
                                return '<a href = "/yeast/associated/detail/?id='+ table_name + ':' + row_name +'&name='+ column_order[i]+ ':' +row[1]+'"> Detail </a>';
                            },
                        }
                    ]
                })
            }
        },
        error :function(){
            alert('Something error');
        }
    })

})