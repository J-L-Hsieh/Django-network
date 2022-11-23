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

    function GO_MFFunction() {window.location.hash = "#GO_MF";}
    // $('#GO_CC_move').click(function(){window.location.hash = "#GO_CC";})
    // $('#Protein_Domain_move').on(function(){console.log('13212212123')})


    $.ajax({
        url : '/yeast/ajax_associated/',
        data : {'table_name' : table_name,'row_name':row_name},
        success:function(response){
            $('#Answer1').html(response.associated_table);
            $('#associated_table').DataTable();
            column_order = response.all_tables.column_order
            /* */


            /*-------------- 製作all table的 div 與專屬id ------------------ */
            var add_html = ''
            var add_herf = ''
            for (i=0 ;i< column_order.length;i++){
                add_html = add_html + `<div id = ${column_order[i]}></div>`
                add_herf = add_herf + `<input id ="${column_order[i]}_move" class="btn btn-outline-primary" type="button" name="Submit" value="${column_order[i]}"  ></input>`
            }
            console.log(add_herf)
            $('#herf_table').html(add_herf)
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

    console.log(table_name)
    console.log(row_name)

})

$(document).on('click','input:button',function(){
    console.log($(this).attr('id').replace('_move',''))
    window.location.href = `#${$(this).attr('id').replace('_move','')}`
});
// $(document).on('click','#GO_CC_move ',function(){
//     window.location.href = "#GO_CC";
// });
// $(document).on('click','#GO_BP_move ',function(){
//     window.location.href = "#GO_CC";
// });