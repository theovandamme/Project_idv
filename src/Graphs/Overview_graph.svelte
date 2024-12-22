<script>

    import { Graphic, Label, Point, DiscreteLegend, getClassLabels } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleOrdinal } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    import { stratify, hierarchy} from 'd3-hierarchy';
    import { schemeSet3 } from 'd3-scale-chromatic'
    import {forceLink, forceCenter, forceSimulation,forceX, forceY, forceManyBody, forceCollide} from 'd3-force';
    export let DC_raw
    export let select_page 
    export let leader
    export let width
    export let raw_data


    let final_text_width = 1000
    $: charts_width = final_text_width/2
    $: console.log(charts_width)
    let test = DC_raw.rows()
    let select = false
    let label
    let page = 0
    let scale_x = [0,1]
    let scale_y = [0,1]

    let legend_regions = DC_raw.domain('Region')
    let legend_religions = DC_raw.domain('religion')
    legend_religions.push('No information')
    let legend_education = ["No/incomplete primary", "Finished primary", "Finished secondary","Obtained Bachelor's","Obtained Master's","Obtained Doctorate"]
    let legend_dead = ['Alive', 'Dead', 'No information']

    // making of color scales
    let color_regions = scaleOrdinal(DC_raw.domain('Region'), schemeSet3)
    let color_religions = scaleOrdinal(DC_raw.domain('religion'), schemeSet3).unknown('grey')
    let color_education = scaleOrdinal(legend_education, schemeSet3).unknown('grey')
    let color_dead = scaleOrdinal(DC_raw.domain('dead'), schemeSet3).unknown('grey')

    function make_color(page, node){
        if (page ==0){
            return 'grey'
        }
        else if (page==1 ){
            return color_regions(node.Region)
        }
        else if (page==2){
            return color_religions(node.religion)
        }
        else if (page==3){
            return color_education(node.education)
        }
        else if (page==4){
            return color_dead(node.dead)
        }
    }
    function add_gray(color_scheme){
        color_scheme.push('grey')
        return color_scheme
    }
    function add_no_information(legend){
        legend.push('No information')
        return legend
    }
    function label_text(label){
        if (label.deathcause == null){
            return 'no information'
        } 
        else {
            return label.deathcause
        }
    }

    function Handlemouseover(node){
        select = true
        //console.log(node)
        label = node
        
    }

    function ChooseSide(label){
        if (label.x <0.5){
            return 'lb'
        }
        else{
            return 'rb'
        }
    }
    function xPos(label){
        let side = ChooseSide(label)
        if (side=='lb'){
            return label.x + 0.01
        }
        else{
            return label.x - 0.01
        }

    }
    function changePage(led){
        leader = led.fullbirthname 
        select_page = 'search'
    }

    let simulationEnd = false
    let simulationRunning = true
    let Initial_grid_columns = 25;
    let Initial_grid_rows = 17;
    let cellWidth = 1 / Initial_grid_columns;
    let cellHeight = 1 / Initial_grid_rows;

    $: if (page == 0 && simulationRunning){
    scale_x = [0, 1]
    scale_y = [0, 1]
    let simulation = forceSimulation(test)
        .force("x", forceX((d, i) => (i % Initial_grid_columns) * cellWidth + cellWidth / 2).strength(1))
        .force("y", forceY((d, i) => Math.floor(i / Initial_grid_columns) * cellHeight + cellHeight / 2).strength(1))
        .force("collision", forceCollide().radius(Math.min(cellWidth, cellHeight) / 2 * 0.9))
        .alphaDecay(0.2)
        .on('tick', () => {
        test = test
        })
        .on('end', () => {
            simulationEnd = true
            simulationRunning = false
            test = test
            })

        }

    $: if (page == 1 && simulationRunning){
        scale_x = [-0.05, 1.05]
        scale_y = [-0.05, 1.05]
        simulationEnd = false;
        let regions = DC_raw.domain('Region')
        let links = []
        for (let i = 0; i < regions.length; i++){
            let region = regions[i]
            let region_DC = DC_raw.filter(row => row.Region === region).column('fullbirthname')
                region_DC.forEach((element)=>{
                    for (let i = 0; i < region_DC.length; i++){
                        let name_source = element
                        let name_target = region_DC[i]
                        links.push({source:name_source, target:name_target})
                    }
                })
                }
        let simulation = forceSimulation(test)
        .force('link', forceLink(links).id(d => d.fullbirthname).distance(0.02))
        .force("collision", forceCollide().radius(0.05 / 2 * 0.9))
        .force('center', forceCenter(0.55, 0.55))
        .alphaDecay(0.35)
        //.force('charge', forceManyBody().strength(1))
        .on('tick', () => {
            if (!simulationEnd){
                test.map((value)=> delete value.$key)
                test = test
                let DC_test = new DataContainer(test)
                let maxX = DC_test.max('x')
                let minX = DC_test.min('x')
                let maxY = DC_test.max('y')
                let minY = DC_test.min('y')
                test.map((value)=> value.x = (value.x - minX)/(maxX-minX))
                test.map((value)=> value.y = (value.y - minY)/(maxY-minY))
            }


        })
        .on('end', ()=> {
            simulationEnd = true
            // simulation.stop()
            simulationRunning = false
            test.map((value)=> delete value.$key)
            test = test
            let DC_test = new DataContainer(test)
            let maxX = DC_test.max('x')
            let minX = DC_test.min('x')
            let maxY = DC_test.max('y')
            let minY = DC_test.min('y')
            test.map((value)=> value.x = (value.x - minX)/(maxX-minX))
            test.map((value)=> value.y = (value.y - minY)/(maxY-minY))
        });


    }
    //simulation for the religion
    $: if (page == 2 && simulationRunning){
        simulationEnd = false
        let religions = DC_raw.domain('religion')
        let links = []
        for (let i = 0; i < religions.length; i++){
            let religion = religions[i]
            let religion_DC = DC_raw.filter(row => row.religion === religion).column('fullbirthname')
                religion_DC.forEach((element)=>{
                    for (let i = 0; i < religion_DC.length; i++){
                        let name_source = element
                        let name_target = religion_DC[i]
                        links.push({source:name_source, target:name_target})
                    }
                })
                }
        let no_info = DC_raw.filter(row => row.religion == null).column('fullbirthname')
        no_info.forEach((element)=>{
            for (let i = 0; i < no_info.length; i++){
                        let name_source = element
                        let name_target = no_info[i]
                        links.push({source:name_source, target:name_target})
            }
        })
        
        let simulation = forceSimulation(test)
        .force('link', forceLink(links).id(d => d.fullbirthname).distance(0.02))
        .force("collision", forceCollide().radius(0.05 / 2 * 0.9))
        .force('center', forceCenter(0.55, 0.55))
        .alphaDecay(0.4)
        //.force('charge', forceManyBody().strength(1))
        .on('tick', () => {
            if (!simulationEnd){
                test.map((value)=> delete value.$key)
                test = test
                let DC_test = new DataContainer(test)
                let maxX = DC_test.max('x')
                let minX = DC_test.min('x')
                let maxY = DC_test.max('y')
                let minY = DC_test.min('y')
                test.map((value)=> value.x = (value.x - minX)/(maxX-minX))
                test.map((value)=> value.y = (value.y - minY)/(maxY-minY))
            }
        })
        .on('end', ()=> {
            simulationEnd = true
            // simulation.stop()
            simulationRunning = false
            test.map((value)=> delete value.$key)
            test = test
            let DC_test = new DataContainer(test)
            let maxX = DC_test.max('x')
            let minX = DC_test.min('x')
            let maxY = DC_test.max('y')
            let minY = DC_test.min('y')
            test.map((value)=> value.x = (value.x - minX)/(maxX-minX))
            test.map((value)=> value.y = (value.y - minY)/(maxY-minY))
        });


    }

    // simulation for the education level
    $: if (page == 3 && simulationRunning){
        simulationEnd = false
        let education = DC_raw.domain('education')
        let links = []
        for (let i = 0; i < education.length; i++){
            let educ = education[i]
            let Education_DC = DC_raw.filter(row => row.education === educ).column('fullbirthname')
                Education_DC.forEach((element)=>{
                    for (let i = 0; i < Education_DC.length; i++){
                        let name_source = element
                        let name_target = Education_DC[i]
                        links.push({source:name_source, target:name_target})
                    }
                })
                }
        let no_info = DC_raw.filter(row => row.education == null).column('fullbirthname')
        no_info.forEach((element)=>{
            for (let i = 0; i < no_info.length; i++){
                        let name_source = element
                        let name_target = no_info[i]
                        links.push({source:name_source, target:name_target})
            }
        })
        
        let simulation = forceSimulation(test)
        .force('link', forceLink(links).id(d => d.fullbirthname).distance(0.02))
        .force("collision", forceCollide().radius(0.05 / 2 * 0.9))
        .force('center', forceCenter(0.55, 0.55))
        .alphaDecay(0.4)
        //.force('charge', forceManyBody().strength(1))
        .on('tick', () => {
            if (!simulationEnd){
                test.map((value)=> delete value.$key)
                test = test
                let DC_test = new DataContainer(test)
                let maxX = DC_test.max('x')
                let minX = DC_test.min('x')
                let maxY = DC_test.max('y')
                let minY = DC_test.min('y')
                test.map((value)=> value.x = (value.x - minX)/(maxX-minX))
                test.map((value)=> value.y = (value.y - minY)/(maxY-minY))
            }
        })
        .on('end', ()=> {
            simulationEnd = true
            // simulation.stop()
            simulationRunning = false
            test.map((value)=> delete value.$key)
            test = test
            let DC_test = new DataContainer(test)
            let maxX = DC_test.max('x')
            let minX = DC_test.min('x')
            let maxY = DC_test.max('y')
            let minY = DC_test.min('y')
            test.map((value)=> value.x = (value.x - minX)/(maxX-minX))
            test.map((value)=> value.y = (value.y - minY)/(maxY-minY))
        });


    }

    // simulation for alive/death 
    $: if (page == 4 && simulationRunning){
        simulationEnd = false
        let dead = DC_raw.domain('dead')
        let links = []
        for (let i = 0; i < dead.length; i++){
            let ded = dead[i]
            let Dead_DC = DC_raw.filter(row => row.dead === ded).column('fullbirthname')
                Dead_DC.forEach((element)=>{
                    for (let i = 0; i < Dead_DC.length; i++){
                        let name_source = element
                        let name_target = Dead_DC[i]
                        links.push({source:name_source, target:name_target})
                    }
                })
                }
        let no_info = DC_raw.filter(row => row.dead == null).column('fullbirthname')
        no_info.forEach((element)=>{
            for (let i = 0; i < no_info.length; i++){
                        let name_source = element
                        let name_target = no_info[i]
                        links.push({source:name_source, target:name_target})
            }
        })
        let simulation = forceSimulation(test)
        .force('link', forceLink(links).id(d => d.fullbirthname).distance(0.02))
        .force("collision", forceCollide().radius(0.05 / 2 * 0.9))
        .force('center', forceCenter(0.55, 0.55))
        .alphaDecay(0.4)
        //.force('charge', forceManyBody().strength(1))
        .on('tick', () => {
            if (!simulationEnd){
                test.map((value)=> delete value.$key)
                test = test
                let DC_test = new DataContainer(test)
                let maxX = DC_test.max('x')
                let minX = DC_test.min('x')
                let maxY = DC_test.max('y')
                let minY = DC_test.min('y')
                test.map((value)=> value.x = (value.x - minX)/(maxX-minX))
                test.map((value)=> value.y = (value.y - minY)/(maxY-minY))
            }
        })
        .on('end', ()=> {
            simulationEnd = true
            // simulation.stop()
            simulationRunning = false
            test.map((value)=> delete value.$key)
            test = test
            let DC_test = new DataContainer(test)
            let maxX = DC_test.max('x')
            let minX = DC_test.min('x')
            let maxY = DC_test.max('y')
            let minY = DC_test.min('y')
            test.map((value)=> value.x = (value.x - minX)/(maxX-minX))
            test.map((value)=> value.y = (value.y - minY)/(maxY-minY))
        });


    }
    // simulation for death cause

    const padding = { left: 110, bottom: 40, top: 15, right: 10 }
    </script>
        <div class='text'>
        {#if (page==0)}
        <h3> You can now see the 425 rebel leaders who were active between 1980 and 2011. This does not give us much of an idea of who these people are. Who did they fight against? </h3>
        <p>Hover over the leaders to see who they are.</p>
        {:else if (page==1)}
            <h3> The leaders are now grouped by region in which the country against which they were fighting with is located. What about more personal attributes?  </h3>
        {:else if (page==2)}
            <h3>Such as their beliefs?</h3>
        {:else if (page==3)}
            <h3>Or the education they achieved?</h3>
        {:else if (page==4)}
            <h3> How much of these leaders are still alive today? and if not, how did they die?</h3>
            <p>Hover over the dead rebel leaders to see how they died. </p>
            
        {/if}
        </div>
        {#if (select_page==='overview')}
        <div width={width-20}>

        <div class='left_container'>
        {#if (simulationEnd && page>0)}
            <button class='left_button' 
            on:click={()=> {
            page -=1 
            simulationRunning=true
            }}>
            <img 
            src='./static/arrow_back.svg'   
            alt='arrow_back' 
            >
            </button>
        {/if}
        </div>
        {#if (page<5)}
        <div width={width-80} min-width=4000 class='graph'>
      <Graphic  width={width-80} height='650' scaleX={scale_x} scaleY={scale_y} >
        {#each test as node}
        <Point
        x = {node.x}
        y = {node.y}
        radius = 10
        fill = {make_color(page,node)}
        onMouseover={()=>Handlemouseover(node)}
        onMouseout={()=> select = false}
        onClick={()=> changePage(node)}
        />
        {/each}

        {#if (select)}
        <Label 
            x = {xPos(label)} 
            y= {label.y-0.015} 
            text={label.fullbirthname} 
            fontSize=24
            fontWeight= 1000
            stroke='white' 
            anchorPoint={ChooseSide(label)}/>
        {/if}
        {#if (select && label.dead == 1 && page==4)}
        <Label 
            x = {xPos(label)} 
            y= {label.y+0.015} 
            text={label_text(label)} 
            fontSize=24
            fontWeight= 1000
            stroke='white' 
            anchorPoint={ChooseSide(label)}/>
        {/if}
      </Graphic >
        </div>
        {:else}
            <div class='final_text' width={width-80}>
            <div >
                <h3> This data orginates from the Rebel Organization Leaders (ROLE) database. The investigators for the creation of this database are Benjamin Acosta, Reyko Huang and Daniel Silverman. It was created with the aim to study how leader attributtes, backgrounds and experiences shape the conflict in which they are active. If you wish more information about ROLE, you can visit their <a href="https://www.rebelleaders.org"> website</a> </h3>
            </div>
            <div class='charts' >
                <h4>
                    We used the ROLE dataset to make some graphs with the goal to explore the data. We also created graphs based on the findings of the studies conducted using the ROLE database. You can explore these graphs for the whole world or a specific region in the <a on:click={()=> select_page='charts'}> charts page</a>. A slightly modified version of the ROLE database can also be downloaded there if you would like to explore the data on your own. 
                </h4>
            </div>
            <div>
                <h4>
                    If you are interested by a specific leader and their characteristics, you can go look for them on the <a on:click={()=> select_page='search'}> search page</a>
                </h4>
            </div>
            </div>  
        {/if}
    <div class='right_container'>
      {#if (simulationEnd) && page < 5}
      <button class='right_button' on:click={()=> {
        if(page<6){
            page +=1 
            simulationRunning=true}
        }}><img 
      src='./static/arrow_forward.svg'   
      alt='arrow_forward' 
      ></button>
      {/if}
    </div>
    {#if (page<5)}
    <Graphic {padding} width={width} height='200'>
        {#if (page==1)}
        <DiscreteLegend
            x1={0}
            x2={0.33}
            y1={0}
            y2={1}
            fill={color_regions.range().slice(0,4)}
            labels={legend_regions.slice(0,4)}
            labelFontSize=18
        >
        </DiscreteLegend>

        <DiscreteLegend
        x1={0.33}
        x2={0.66}
        y1={0}
        y2={1}
        fill={color_regions.range().slice(4,8)}
        labels={legend_regions.slice(4,8)}
        labelFontSize=18
        >
        </DiscreteLegend>

        <DiscreteLegend
        x1={0.66}
        x2={0.99}
        y1={0}
        y2={1}
        fill={color_regions.range().slice(8,12)}
        labels={legend_regions.slice(8,12)}
        labelFontSize=18
        >
        </DiscreteLegend>
        {/if}

        {#if (page==2)}
        <DiscreteLegend
            x1={0}
            x2={0.33}
            y1={0}
            y2={1}
            fill={color_religions.range().slice(0,2)}
            labels={legend_religions.slice(0,2)}
            labelFontSize=18
        >
        </DiscreteLegend>

        <DiscreteLegend
        x1={0.33}
        x2={0.66}
        y1={0}
        y2={1}
        fill={color_religions.range().slice(2,4)}
        labels={legend_religions.slice(2,4)}
        labelFontSize=18
        >
        </DiscreteLegend>

        <DiscreteLegend
        x1={0.66}
        x2={0.99}
        y1={0}
        y2={1}
        fill={add_gray(color_religions.range().slice(4,5))}
        labels={legend_religions.slice(4,6)}
        labelFontSize=18
        >
        </DiscreteLegend>
        {/if}

        {#if (page==3)}
        <DiscreteLegend
            x1={0}
            x2={0.33}
            y1={0}
            y2={1}
            fill={color_education.range().slice(0,3)}
            labels={legend_education.slice(0,3)}
            labelFontSize=18
        >
        </DiscreteLegend>

        <DiscreteLegend
        x1={0.33}
        x2={0.66}
        y1={0}
        y2={1}
        fill={color_education.range().slice(3,5)}
        labels={legend_education.slice(3,5)}
        labelFontSize=18
        >
        </DiscreteLegend>

        <DiscreteLegend
        x1={0.66}
        x2={0.99}
        y1={0}
        y2={1}
        fill={add_gray(color_education.range().slice(5,6))}
        labels={add_no_information(legend_education.slice(5,6))}
        labelFontSize=18
        >
        </DiscreteLegend>
        {/if}

        {#if (page==4)}
        <DiscreteLegend
            x1={0}
            x2={0.33}
            y1={0}
            y2={1}
            fill={color_dead.range().slice(0,1)}
            labels={legend_dead.slice(0,1)}
            labelFontSize=18
        >
        </DiscreteLegend>

        <DiscreteLegend
        x1={0.33}
        x2={0.66}
        y1={0}
        y2={1}
        fill={color_dead.range().slice(1,2)}
        labels={legend_dead.slice(1,2)}
        labelFontSize=18
        >
        </DiscreteLegend>

        <DiscreteLegend
        x1={0.66}
        x2={0.99}
        y1={0}
        y2={1}
        fill={'grey'}
        labels={legend_dead.slice(2,3)}
        labelFontSize=18
        >
        </DiscreteLegend>
        {/if}
        


      </Graphic>
    {/if}
     </div>
        {/if}

    <style>
    a{text-decoration: underline;
      cursor: pointer;}
    .final_text{padding-left: 60px;}
    .text{padding-left:20px;}
    .left_container{
        width:charts_width;
        height:650px;
        float:left;
        
    }
    .right_container{
        width:38px;
        height:650px;
        float:right;
        
    }
    .left_button{
        margin-left: 10px;
        background-color: #116466;
        stroke:#116466;
        margin-right: -10px;
        position: relative;
        float: left;
        margin-top: 325px;
    }
    .graph{
        float:left;
    }
    .right_button{
        background-color: #116466;
        stroke:#116466;
        position: relative;
        float: right;
        margin-top: 325px;

    }
    </style>