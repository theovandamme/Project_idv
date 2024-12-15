<script>

    import { Graphic, Label, Point, Line, XAxis, YAxis, x2s } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    import { pack } from 'd3-hierarchy';
    import {forceLink, forceCenter, forceSimulation,forceX, forceY, forceManyBody, forceCollide} from 'd3-force'
    export let DC_raw
    export let select_page 
    export let leader
    export let width

    let test = DC_raw.rows()
    let select = false
    let label
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
  });

    </script>
        {#if (select_page==='overview')}
      <Graphic  width={width} height='650' scaleX={[-0.05, 1.15]} scaleY={[-0.05, 1.05]} padding={20}>
        {#each test as node}
        <Point
        x = {node.x}
        y = {node.y}
        radius = 10
        fill = 'grey'
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