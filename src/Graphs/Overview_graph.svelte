<script>

    import { Graphic, Label, Point, Line, XAxis, YAxis, x2s } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleOrdinal } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    import { stratify, hierarchy} from 'd3-hierarchy';
    import {group} from 'd3-array';
    import { schemeSet3 } from 'd3-scale-chromatic'
    import {forceLink, forceCenter, forceSimulation,forceX, forceY, forceManyBody, forceCollide} from 'd3-force';
    export let DC_raw
    export let select_page 
    export let leader
    export let width
    export let raw_data

    let test = DC_raw.rows()
    let select = false
    let label
    let page = 0
    let scale_x = [0,1]
    let scale_y = [0,1]
    const colors = {
    "Middle East": "gold",
    "Oceania": "#33FF57",
    "Europe": "#3357FF",
    "Central Asia": "#FFFF33",
    "Sub-Saharan Africa": "#FF5733",
    "Northern Africa": "#8E44AD",
    "South America": "#00FFFF",
    "South-Eastern Asia": "#FF00FF",
    "Eastern Europe": "#00FF00",
    "Central America": "#008080",
    'North America': "#000080",
    'South Asia': "#C0C0C0"
};
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

    let simulation = forceSimulation(test)
        .force("x", forceX((d, i) => (i % Initial_grid_columns) * cellWidth + cellWidth / 2).strength(1))
        .force("y", forceY((d, i) => Math.floor(i / Initial_grid_columns) * cellHeight + cellHeight / 2).strength(1))
        .force("collision", forceCollide().radius(Math.min(cellWidth, cellHeight) / 2 * 0.9))
        .on('tick', () => {
        test = test
        })
        .on('end', () => {
            console.log('done')
            test = test
            })

    

    $: if (page == 1 && simulationRunning){
        scale_x = [-0.05, 1.05]
        scale_y = [-0.05, 1.05]
        simulationEnd = false;
        let grouped_regions = group(raw_data, (d) => d.Region);
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
        simulation = forceSimulation(test)
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
            console.log('1done')
        });


    }
    </script>
        {#if (select_page==='overview')}
        <button on:click={()=> page +=1}>text</button>
      <Graphic  width={width} height='650' scaleX={scale_x} scaleY={scale_y}  padding={20}>
        {#each test as node}
        <Point
        x = {node.x}
        y = {node.y}
        radius = 10
        fill = {colors[node.Region]}
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
      </Graphic>
        {/if}

    <style>
    </style>