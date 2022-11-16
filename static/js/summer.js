$( document ).ready(function() {

    $.ajaxSetup({
        data: {
        csrfmiddlewaretoken: '{{ csrf_token }}'
        },
    });

    $('#ex_1').click(function(){
        document.getElementById('input').innerHTML ="<textarea id='name_input' rows='12' cols='50'>" + "YAL064W\nYFL013W-A\nYLR154W-C\nQ0010\nAAP1\nAAS1\nTy1\n3'-5' DNA helicase\n1-phosphatidylinositol 4-kinase LSB6\nXXXX" + '</textarea>';

    })
    $('#ex_2').click(function(){
        document.getElementById('input').innerHTML ="<textarea id='name_input' rows='12' cols='50'>" + 'YBR021W\nYKL051W\nYJR009C\nYMR109W\nYGR192C\nYJL052W\nYKR014C\nYOL103W\nYGR191W\nYLR332W\nYKL220C\nYAL038W\nYCR012W\nYIL033C\nYDR348C\nYLR413W\nYNL192W\nYHR005C\nYIR019C\nYJL005W\nYGR254W\nYHR174W\nYLL052C\nYPR192W\nYDR050C\nYML132W\nYER020W\nYDL194W\nYLR452C\nYJL129C\nYKL126W\nYKL209C\nYGL115W\nYML116W\nYLR081W\nYDR122W\nYLR096W\nYFR012W\nYDR040C\nYGR152C\nYGL167C\nYJR152W\nYPL036W\nYER056C\nYCR075C\nYOR212W\nYJR086W\nYLR229C\nYKR039W\nYDR164C\nYOR317W\nYJL085W\nYNL194C\nYER091C\nYLR303W\nYMR307W\nYNL183C\nYLR342W\nYFL014W\nYHR135C\nYNL154C\nYIL009W\nYMR011W\nYNL084C\nYLL043W\nYPR165W\nYCR098C\nYCR037C\nYCL048W\nYGR032W\nYCL073C\nYCR010C\nYFR022W\nYCR021C\nYJR100C\nYJR125C\nYMR246W\nYFL005W\nYGL045W\nYPL204W\nYGR068C\nYDR497C\nYGR121C\nYDR522C\nYAL030W\nYDR090C\nYDR039C\nYOR018W\nYDR153C\nYHR094C\nYDR345C\nYHR092C\nYMR306W\nYPR159W\nYLR206W\nYDR011W\nYKL203C\nYER166W\nYLR214W\nYLL007C\nYPL232W\nYKR093W\nYCR024C-A\nYNR002C\nYDR103W\nYOR153W\nYHL016C\nYJR160C\nYDL247W\nYGL208W\nYKR059W\nYJL138C\nYAL005C\nYLL024C\nYJR066W\nYBL069W\nYDL229W\nYHR214W\nYDR212W\nYKL217W\nYBR196C\nYIL034C\nYKR105C\nYKR106W\nYJR040W\nYLR305C\nYDR158W\nYBR054W\nYBR069C\nYOR322C\nYDL161W\nYDR038C\nYBR008C\nYBL106C\nYBL042C\nYBR016W\nYBR043C\nYBR086C\nYMR186W\nYBR294W\nYBR295W\nYBR296C\nYHR201C\nYHR073W\nYHL044W\nYHL040C\nYHR048W\nYHR114W\nYCL040W\nYOL122C\nYOL020W\nYMR058W\nYDR208W\nYDR342C\nYMR008C\nYJL198W\nYCR088W\nYAR031W\nYAR033W\nYAL056W\nYMR183C\nYIL147C\nYDR536W\nYER155C\nYER123W\nYER060W\nYER118C\nYER120W\nYER143W\nYER145C\nYDR461W\nYER185W\nYNL145W\nYBL060W\nYJL093C\nYBL061C\nYHR042W\nYKL187C\nYIL120W\nYIL105C\nYIL088C\nYNL322C\nYIL047C\nYMR319C\nYOR188W\nYLR353W\nYDR420W\nYNL291C\nYPL092W\nYNL142W\nYNL323W\nYJL100W\nYFL050C\nYGR197C\nYGR198W\nYJL170C\nYJL145W\nYJL058C\nYJR059W\nYNL294C\nYNL293W\nYPR124W\nYGR217W\nYGR224W\nYGR055W\nYGL233W\nYOR371C\nYOR328W\nYBL105C\nYGR060W\nYGR213C\nYGR281W\nYGL186C\nYBL091C-A\nYGL084C\nYGL053W\nYGL051W\nYGR041W\nYGR065C\nYGR138C\nYGR266W\nYNR049C\nYNR047W\nYNR060W\nYNR070W\nYNL275W\nYCR004C\nYNL180C\nYNL173C\nYCR027C\nYNL065W\nYNL047C\nYML052W\nYOR008C\nYCL058C\nYNL093W\nYDR276C\nYCR017C\nYKR055W\nYCR028C\nYDR463W\nYPL058C\nYOR047C\nYJR005W\nYDR459C\nYBR023C\nYML072C\nYMR212C\nYMR215W\nYDR160W\nYDR104C\nYML006C\nYMR192W\nYMR017W\nYMR243C\nYDL222C\nYLR120C\nYGR014W\nYMR063W\nYOR316C\nYMR251W-A\nYKL094W\nYKL007W\nYLR237W\nYLR138W\nYIR006C\nYLR422W\nYPR156C\nYLR414C\nYJR054W\nYPR194C\nYPR201W\nYDR309C\nYER177W\nYLL010C\nYLL028W\nYLR019W\nYLR020C\nYML047C\nYOL019W\nYOL078W\nYOL130W\nYOL158C\nYOR011W\nYOR049C\nYOR071C\nYOR306C\nYOR378W\nYOR381W\nYOR390W\nYPL274W\nYPL279C\nYPR032W\nYOR104W\nYAR050W\nYDR033W\nYER060W-A\nYMR031C\nYPR149W\nYOR171C\nYOR273C\nYDL138W\nYLR092W\nYOL152W\nYPL249C\nYDR055W\nYDR384C\nYDL035C\nYLL061W\nYLR130C\nYOL002C\nYDL019C\nYOL113W\nYDL012C\nYDR093W\nYML125C\nYGR031C-A\nYOR129C\nYOR030W\nYDR129C\nYEL047C\nYKL035W\nYKL046C\nYDR099W\nYKL105C\nYBL007C\nYLR058C\nYKL196C\nYKR100C\nYNL090W\nYDR414C\nYPL158C\nYBL099W\nYAL014C\nYAL022C\nYAR042W\nYBR264C\nYBR129C\nYLR025W\nYOR275C\nYMR120C\nYLR109W\nYBL085W\nYBR299W\nYHR096C\nYNL257C\nYDR343C\nYER125W\nYNL209W\nYIR038C\nYNL271C\nYOR327C\nYJL171C\nYJL158C\nYJR065C\nYLR432W\nYGL082W\nYGR086C\nYGR122W\nYGR256W\nYGR292W\nYPL265W\nYNL231C\nYIL118W\nYLL050C\nYML128C\nYHL007C\nYPR075C\nYDL124W\nYDL223C\nYOL109W\nYPL004C\nYDR032C\nYOR161C\nYDL135C\nYOR086C\nYBL029C-A\nYOL009C\nYPL240C\nYGR131W\nYML003W\nYML002W\nYBL075C\nYLL053C\nYGR241C\nYHR126C\nYHR161C\nYJR001W\nYIL140W\nYAR066W\nYCL025C\nYKL064W\nYNL128W\nYDR506C\nYDL192W\nYOR353C\nYER067W\nYBR005W\nYER093C\nYDR210W\nYIR039C\nYJL212C\nYNL006W\nYFL054C\nYFL051C\nYFR029W\nYGL160W\nYJL156C\nYNL012W\nYNL087W\nYLR443W\nYLR047C\nYGL108C\nYKL060C\nYNL283C\nYNL279W\nYNL033W\nYNL019C\nYJR058C\nYPL056C\nYDL185W\nYGR167W\nYMR238W\nYMR034C\nYLR194C\nYLR219W\nYDL137W\nYLR343W\nYMR244C-A\nYOR348C\nYDR373W\nYER103W\nYCR091W\nYCR030C\nYCR094W\nYKR050W\nYPR171W\nYNR048W\nYGL255W\nYER008C\nYGR143W\nYBR207W\nYIL043C\nYHL047C\nYHR050W\nYHR155W\nYAL026C\nYEL065W\nYGR009C\nYIL121W\nYIL048W\nYFL047W\nYMR279C\nYMR266W\nYMR006C\nYML087C\nYIR028W\nYMR032W\nYOR301W\nYLR241W\nYLR411W\nYLL005C\nYOL011W\nYOR192C\nYOR384W\nYPL180W\nYLR034C\nYOL084W\nYLR046C\nYLL051C\nYMR162C\nYGR212W\nYCL048W-A\nYDR524C-B\nYPR055W\nYIL171W\nYLR299W\nYBR068C\nYLL055W\nYNL243W\nYBL037W\nYHR006W\nYAR027W\nYEL017C-A\nYFL041W\nYJR151C\nYGR221C\nYDR261C\nYGR026W\nYDR144C\nYMR086W\nYMR068W\nYLR373C\nYLR187W\nYLR004C\nYOL132W\nYPL176C\nYLR121C\nYLR084C\nYLR262C' + '</textarea>';
    })

    $('#domain_analyze').click(function(){
        var name_input_domain = $("#name_input").val();
        var name_data = new FormData();
        name_data.append('name_input',name_input_domain);
        document.getElementById("domain_analyze").innerHTML = "請耐心等待"
        document.getElementById('output').innerHTML = ''
        Domain_id_output = ''
        $.ajax({
            url:'/summer/ajax_domain/', 
            data:name_data,  // 傳到後端的資料
            type:'POST',
            dataType: 'json',
            processData:false,
            contentType:false,
            success:function(data)
            { //後端傳來的jsonresponse
                
                Domain_id_body = ''
                Domain_id_output = ''
                document.getElementById('output').innerHTML = ''
                var Domain_id = data.Domain_id
                var P_value = data.P_value
                var fdr = data.fdr
                var bonferroni = data.Bonferroni
                var expected = data.expected
                var observed = data.observed
                var type = $('#P_type').val()
                var cut_off = $('#cut_off').val()

                result = '';
                if (type == 'none')
                    result = P_value;
                else if (type == 'fdr')
                    result = fdr;
                else if (type == 'bonferroni')
                    result = bonferroni;
                        
                for (var i = 0; i < Domain_id.length; i++){
                    if (result[i] <= cut_off) {
                        Domain_id_body += '<tr><td>' + Domain_id[i] + '</td><td>' + expected[i] + '</td><td>' + observed[i] + '</td><td>' + result[i] + '</td></tr>' 
                    }
                }
                Domain_id_output = '<p id=output_table><table><thead><tr><th>Domain</th><th>expected</th><th>observed</th><th>p-value</th></tr></thead><tbody id=output_tbody>' + Domain_id_body + '</tbody></table></p>'
                document.getElementById('output').innerHTML = Domain_id_output;
                document.getElementById("domain_analyze").innerHTML = 'p-value分析'
                $('table').DataTable({
                    "order": [[3, 'asc']]
                })


                $('#P_type, #cut_off').on('change', function() {

                    Domain_id_body = ''
                    var type = $('#P_type').val()
                    var cut_off = $('#cut_off').val()
                    result = ''
                    if (type == 'none')
                        result = P_value;
                    else if (type == 'fdr')
                        result = fdr;
                    else if (type == 'bonferroni')
                        result = bonferroni;
                    for (var i = 0; i < Domain_id.length; i++) {
                        if (result[i] <= cut_off) {
                            Domain_id_body += '<tr><td>' + Domain_id[i] + '</td><td>' + expected[i] + '</td><td>' + observed[i] + '</td><td>' + result[i] + '</td></tr>' 
                        }
                    }
                    Domain_id_output =''
                    Domain_id_output = '<p id=output_table><table><thead><tr><th>Domain</th><th>expected</th><th>observed</th><th>p-value</th></tr></thead><tbody id=output_tbody>' + Domain_id_body + '</tbody></table></p>'
                    document.getElementById('output').innerHTML = Domain_id_output;
                    $('table').DataTable({
                        "order": [[3, 'asc']]
                    })
                })
                
            }
        });
    })
    $('#submit').click(function(){

        var name_input = $("#name_input").val();
        var parse_data = new FormData();
        parse_data.append('name_input',name_input);
        document.getElementById("submit").innerHTML = "請耐心等待"

        $.ajax({
            url:'/summer/ajax_test/', 
            data:parse_data,  // 傳到後端的資料
            type:'POST',
            dataType: 'json',
            processData:false,
            contentType:false,
            success:function(data)
            { //後端傳來的jsonresponse
                Good_ID = ''
                Good_ID_body = ''
                Good_Name = ''
                Good_Name_body = ''
                Error_Name = ''
                Error_Name_body = ''
                Error_ID = ''
                Error_ID_body = ''
                Other = ''
                Other_body = ''
                var Good_Name_list = data.Good_Name_list
                var Good_ID_list = data.Good_ID_list
                var Error_Name_list = data.Error_Name_list
                var Error_ID_list = data.Error_ID_list
                var Good_Name_input = data.Good_Name_input
                var Good_ID_input = data.Good_ID_input
                var Error_Name_input = data.Error_Name_input
                var Error_ID_input = data.Error_ID_input
                var Other_input = data.Other_input

                for (var i = 0; i < Good_ID_list.length; i++){
                    Good_ID_body += '<tr>' + '<td>' + Good_ID_input[i] + '</td>' + '<td>' + Good_ID_list[i] +  '</td>' + '</tr>' 
                }
                if (Good_ID_body == '') {
                    Good_ID = ''
                }else{
                    Good_ID = '<h2>正確ID</h2>' + '<table><thead><tr><th>Name</th><th>ID</th></tr></thead><tbody>' + Good_ID_body + '</tbody></table>'
                }

                for (var i = 0; i < Good_Name_list.length; i++){
                    Good_Name_body += '<tr>' + '<td>'+ Good_Name_input[i] + '</td>' + '<td>' + Good_Name_list[i] + '</td>' + '</tr>'
                }
                if (Good_Name_body == '') {
                    Good_Name = ''
                }else{
                    Good_Name = '<h2>轉成單一ID</h2>' + '<table><thead><tr><th>Name</th><th>ID</th></tr></thead><tbody>' + Good_Name_body + '</tbody></table>'
                }
                for (var i = 0; i < Error_Name_list.length; i++){
                    Error_Name_body += '<tr>' + '<td>' + Error_Name_input[i] + '</td>' + '<td>' + Error_Name_list[i] + '</td>' + '</tr>'
                }
                if (Error_Name_body == '') {
                    Error_Name = ''
                }else{
                    Error_Name = '<h2>轉成多個ID</h2>' + '<table><thead><tr><th>Name</th><th>ID</th></tr></thead><tbody>' + Error_Name_body + '</tbody></table>'
                }
                for (var i = 0; i < Error_ID_list.length; i++){
                    Error_ID_body += '<tr>' + '<td>' + Error_ID_input[i] + '</td>' + '<td>' + Error_ID_list[i] + '</td>' + '</tr>' 
                }
                if (Error_ID_body == '') {
                    Error_ID = ''
                }else{
                    Error_ID = '<h2>轉成多個ID的ID</h2>' + '<table><thead><tr><th>Name</th><th>ID</th></tr></thead><tbody>' + Error_ID_body + '</tbody></table>'
                }
                
                for (var i = 0; i < Other_input.length; i++){  
                    Other_body += '<tr>' + '<td>' + Other_input[i] + '</td>' + '<td>' + "Error" + '</td>' + '</tr>' 
                }
                if (Other_body == '') {
                    Other = ''
                }else{
                    Other = '<h2>無法辨識</h2>' + '<table><thead><tr><th>Name</th><th>ID</th></tr></thead><tbody>' + Other_body + '</tbody></table>'
                }
                output = Good_ID + Good_Name + Error_Name + Error_ID + Other
                document.getElementById('output').innerHTML = output;
                document.getElementById("submit").innerHTML = '除錯分析'
                $('table').DataTable({
                    aoColumns : [
                        { "sWidth": "15%"},
                        { "sWidth": "15%"}
                    ]
                  })

            },
            error:function()
            {
                //alert('something error');
            },
    
         });

    })
    
    });