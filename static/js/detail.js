$.ajaxSetup({
    headers: { 'X-CSRFToken': csrf_token },
    type: 'POST',
});

$(document).ready(function(){
    var url = document.URL
    console.log(url)
    url = url.split('/')
    var transcript = url[4]
    console.log(transcript)
    $.ajax({
        url : '/detail/ajax_detail/',
        data : {'transcript' : transcript},
        success:function(response){
            $('#spliced_table').html(response.spliced_feature_table)
            $('#unspliced_table').html(response.unspliced_feature_table)
            $('#table_id1').DataTable();
            $('#table_id2').DataTable();
            spliced_sequecne_table(response.spliced_sequence,response.spliced_feature);
            unspliced_sequecne_table(response.unspliced_sequence,response.unspliced_feature)
            cds_table(response.cds)
            cds_sequence_table(response.cds_sequence)
            D3_spliced(response.spliced_feature)
            D3_unspliced(response.unspliced_feature)
        },
        error :function(){
            alert('Something error');
        }
    })
    function spliced_sequecne_table(sequence,feature){
        let length = Object.keys(feature).length;
        // console.log(feature)
        let arr = [];
        let arr_feature = [];
        // console.log(length)
        for(i=0; i<length-1;i++){
            // console.log(feature[i]['start']);
            // console.log(typeof(feature[i+1]['start']));
            if(feature[i]['start'] == feature[i+1]['start']){

                if(feature[i]['type'] == 'five_prime_UTR'){
                    arr_feature.push(feature[i]['type'])
                    arr_feature.push(feature[i+1]['type'])
                    // arr.push(feature[i]['stop']-feature[i]['start']+1);
                    // arr.push(feature[i+1]['stop']-feature[i]['stop']+1);
                    arr.push(feature[i]['stop']);
                    arr.push(feature[i+1]['stop']);
                    i= i+1;

                }
                else{
                    arr_feature.push(feature[i+1]['type'])
                    arr_feature.push(feature[i]['type'])
                    // arr.push(feature[i+1]['stop']-feature[i+1]['start']+1);
                    // arr.push(feature[i]['stop']-feature[i+1]['stop']+1);
                    arr.push(feature[i+1]['stop']);
                    arr.push(feature[i]['stop']);
                    i= i+1;
                }
            }

            else if(feature[i]['stop'] == feature[i+1]['stop']){
                if(feature[i]['type'] == 'three_prime_UTR'){
                    arr_feature.push(feature[i-1]['type'])
                    arr_feature.push(feature[i]['type'])
                    // arr.push(feature[i]['start']-feature[i+1]['start']+1);
                    // arr.push(feature[i]['stop']-feature[i]['start']+1);3
                    arr.push(feature[i]['start']-1);
                    arr.push(feature[i]['stop']);
                    i=i+1;
                }
                else{
                    arr_feature.push(feature[i]['type'])
                    arr_feature.push(feature[i+1]['type'])
                    // arr.push(feature[i]['stop']-feature[i]['start']+1);
                    // arr.push(feature[i+1]['start']-feature[i]['start']+1);
                    arr.push(feature[i+1]['start']-1);
                    arr.push(feature[i]['stop']);
                    i=i+1;
                }
            }
            else{
                if (Number(i) == length-2){
                    console.log(length)
                    arr.push(feature[i]['stop'])
                    arr.push(feature[length-1]['stop'])
                    arr_feature.push(feature[i]['type'])
                    arr_feature.push(feature[length-1]['type'])

                }else{
                arr_feature.push(feature[i]['type'])
                // arr.push(feature[i]['stop']-feature[i]['start']+1)
                arr.push(feature[i]['stop']);
                }

            }

        }



        let j = 0;
        for(i=0;i<sequence.length;i++){
            if(i < arr[j]){
                $('#spliced').append('<span class='+'"'+arr_feature[j]+'"'+'>'+sequence[i]+'</span>')
            }
            else{
                $('#spliced').append('<span class='+'"'+arr_feature[j+1]+'"'+'>'+sequence[i]+'</span>');
                j = j+1;
            }
            if(i%50 == 0 ){
                $('.tag1').append('<span>'+String(i+1)+'</span><br>');
            }
        }


    }
    function unspliced_sequecne_table(sequence,feature){
        let length = Object.keys(feature).length;
        let arr = [];
        let arr_feature = [];

        for(i=0; i<length-1;i++){
            // console.log(feature[i]['start']);
            // console.log(typeof(feature[i+1]['start']));

            if(feature[i]['start'] == feature[i+1]['start']){
                if(feature[i]['type'] == 'five_prime_UTR'){
                    arr_feature.push(feature[i]['type'])
                    arr_feature.push(feature[i+1]['type'])
                    // arr.push(feature[i]['stop']-feature[i]['start']+1);
                    // arr.push(feature[i+1]['stop']-feature[i]['stop']+1);
                    arr.push(feature[i]['stop']);
                    arr.push(feature[i+1]['stop']);
                    i= i+1;

                }
                else{
                    arr_feature.push(feature[i+1]['type'])
                    arr_feature.push(feature[i]['type'])
                    // arr.push(feature[i+1]['stop']-feature[i+1]['start']+1);
                    // arr.push(feature[i]['stop']-feature[i+1]['stop']+1);
                    arr.push(feature[i+1]['stop']);
                    arr.push(feature[i]['stop']);
                    i= i+1;
                }
            }

            else if(feature[i]['stop'] == feature[i+1]['stop']){
                if(feature[i]['type'] == 'three_prime_UTR'){
                    arr_feature.push(feature[i+1]['type'])
                    arr_feature.push(feature[i]['type'])
                    // arr.push(feature[i]['start']-feature[i+1]['start']+1);
                    // arr.push(feature[i]['stop']-feature[i]['start']+1);3
                    arr.push(feature[i]['start']-1);
                    arr.push(feature[i]['stop']);
                    i=i+1;
                }
                else{

                    arr_feature.push(feature[i]['type'])
                    arr_feature.push(feature[i+1]['type'])
                    // arr.push(feature[i]['stop']-feature[i]['start']+1);
                    // arr.push(feature[i+1]['start']-feature[i]['start']+1);
                    arr.push(feature[i+1]['start']-1);
                    arr.push(feature[i]['stop']);
                    i=i+1;
                }
            }
            else{
                if (Number(i) == length-2){
                    // console.log(length)
                    arr.push(feature[i]['stop'])
                    arr.push(feature[length-1]['stop'])
                    arr_feature.push(feature[i]['type'])
                    arr_feature.push(feature[length-1]['type'])

                }else{
                arr_feature.push(feature[i]['type'])
                // arr.push(feature[i]['stop']-feature[i]['start']+1)
                arr.push(feature[i]['stop']);
                }

            }
        }

        let j = 0;
        for(i=0;i<sequence.length;i++){
            if(i < arr[j]){
                $('#unspliced').append('<span class='+'"'+arr_feature[j]+'"'+'>'+sequence[i]+'</span>')
            }
            else{
                $('#unspliced').append('<span class='+'"'+arr_feature[j+1]+'"'+'>'+sequence[i]+'</span>');
                j = j+1;
            }

            if(i%50 == 0 ){
                $('.tag2').append('<span>'+String(i+1)+'</span><br>');
            }
        }
    }
    //------------------------------------------------------------------------------
    function cds_table(sequence){
        for(i=0;i<sequence.length;i++){
            $('#cds').append('<span>'+sequence[i]+'</span>')
            if(i%20 == 0 ){
                $('.tag3').append('<span>'+' '+String(i+1)+'</span><br>');
            }
        }
    }

    function cds_sequence_table(sequence){
        // console.log(sequence.length)
        for(i=0;i<sequence.length;i++){
            $('.cds_sequence').append('<span>'+sequence[i]+'</span>')
            if(i%60 == 0 ){
                $('.tag4').append('<span>'+String(i+1)+'</span><br>');
            }
        }
    }
    // -----------------------------------------------------------------------------
    function D3_unspliced(feature){
        console.log(feature)
        let feature_data = feature;
        const colorScale = d3.scaleOrdinal()
                            .domain(['five_prime_UTR','exon_odd','exon_even','intron','three_prime_UTR'])
                            .range(['gray','yellow','orange','black','gray'])
        const hrightScale = d3.scaleOrdinal()
                            .domain(['five_prime_UTR','exon_odd','exon_even','intron','three_prime_UTR'])
                            .range(['10','20','20','5','10'])
        const yScale = d3.scaleOrdinal()
                            .domain(['five_prime_UTR','exon_odd','exon_even','intron','three_prime_UTR'])
                            .range(['25','20','20','28','25'])
        const length = feature_data.map(i=> i.stop)
        const xscale = d3.scaleLinear()
                        .domain([0,d3.max(length)])
                        .range([0,1200])


        const svg = d3
            .select('.stack_unspliced')
            .append('svg')
            .attr('width', 1200)
            .attr('height', 50)
            .selectAll('rect')
            .data(feature_data)
            .enter()
            .append('rect')
            .attr('width', d => xscale(d.stop -d.start))
            .attr('x', d => xscale(d.start))
            .attr('fill', d => colorScale(d.type))
            .attr('y', d => yScale(d.type))
            .attr('height',d => hrightScale(d.type))
            .attr('id','rect_unspliced')
            .style('cursor', 'pointer');
        // console.log(svg)

        const tooltips = d3.select(".stack_unspliced")
                            .append('div')
                            .style("opacity", 0)
                            .style('position', 'relative')
                            .attr("class", "tooltip")
                            .style("background-color", "light-blue")
                            .style("border", "solid")
                            .style("border-width", "2px")
                            .style("padding", "5px")
                            .style("width","15%")


        d3.selectAll('#rect_unspliced')
            .on('mouseover',function(){
                tooltips.style('opacity',1)
            })
            .on('mousemove', function(d){
                let pt = d3.pointer(this)
                tooltips.style("opacity", 1)
                        .html(`Type:${d.target.__data__.type}<br>Start:${d.target.__data__.start}<br>End:${d.target.__data__.stop}`)
                        .style('right', pt[0]+30+'px')
                        .style('top', pt[1]+'px')
            })
            .on('mouseleave', function(){ //設定滑鼠離開時tooltips隱藏
                tooltips.style("opacity", 0)
            });
    };
    // ---------------------------------D3_spliced-------------------------------
    function D3_spliced(feature){
        // console.log(feature)
        let feature_data1 = feature;
        // const stack = d3.stack()
        //                 .keys(['start','stop','type'])
        // const stackedSeries = stack(dataStack);
        // console.log(stackedSeries)five_prime_UTR
        const colorScale = d3.scaleOrdinal()
                            .domain(['five_prime_UTR','exon_odd','exon_even','intron','three_prime_UTR'])
                            .range(['gray','yellow','orange','black','gray'])
        const hrightScale = d3.scaleOrdinal()
                            .domain(['five_prime_UTR','exon_odd','exon_even','intron','three_prime_UTR'])
                            .range(['10','20','20','5','10'])
        const yScale = d3.scaleOrdinal()
                            .domain(['five_prime_UTR','exon_odd','exon_even','intron','three_prime_UTR'])
                            .range(['25','20','20','28','25'])
        const length = feature_data1.map(i=> i.stop)
        const xscale = d3.scaleLinear()
                        .domain([0,d3.max(length)])
                        .range([0,1200])


        const svg2 = d3
            .select('.stack_spliced')
            .append('svg')
            .attr('width', 1200)
            .attr('height', 50)
            .selectAll('rect')
            .data(feature_data1)
            .enter()
            .append('rect')
            .attr('width', d => xscale(d.stop - d.start))
            .attr('x', d => xscale(d.start))
            .attr('fill', d => colorScale(d.type))
            .attr('y', d => yScale(d.type))
            .attr('height',d => hrightScale(d.type))
            .attr('id','rect_spliced')
            .style('cursor', 'pointer');
        console.log(svg2)

        const tooltips2 = d3.select(".stack_spliced")
                            .append('div')
                            .style("opacity", 0)
                            .style('position', 'relative')
                            .style("background-color", "light-blue")
                            .style("border", "solid")
                            .style("border-width", "2px")
                            .style("padding", "5px")
                            .style("width","15%")
                            .style('ustify-content','right')
                            .style('align-items', 'center')


        d3.selectAll('#rect_spliced')
            .on('mouseover',function(){
                tooltips2.style('opacity',1)
            })
            .on('mousemove', function(d){
                let pt2 = d3.pointer(this)
                tooltips2.style("opacity", 1)
                        .html(`Type:${d.target.__data__.type}<br>Start:${d.target.__data__.start}<br>End:${d.target.__data__.stop}`)
                        .style('left', pt2[0]+30+'px')
                        .style('top', pt2[1]+'px')
            })
            .on('mouseleave', function(){ //設定滑鼠離開時tooltips隱藏
                tooltips2.style("opacity", 0)
            });
    };
});
