<script>

    import { Graphic, Section, RectangleLayer, Point, Line, XAxis, YAxis, x2s } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    import { pack } from 'd3-hierarchy';
    import {forceLink, forceCenter, forceSimulation,forceX, forceY, forceManyBody, forceCollide} from 'd3-force'
    export let DC_raw
    export let width
    let height = 650
    console.log(DC_raw)
    //let simulation = forceSimulation(DC_raw.rows()).on('end', () =>{DC_raw=DC_raw})
    //console.log(simulation)
    //console.log(DC_raw.rows())
    let test = DC_raw.rows()
    let simulation = forceSimulation(test)
    .force("x", forceX().x(d => Math.random() * 1).strength(0.1))
    .force("y", forceY().y(d => Math.random() * 1).strength(0.1))
    .force('collision', forceCollide().radius(0.027))
    .on('tick', () => {
    test = test
   
  });

console.log(simulation);
   function make_coord(DC_raw){

   }
    </script>
      <Graphic  width={width} height='650' scaleX={[-0.12, 1.1]} scaleY={[-0.12, 1.15]} padding={20}>
        {#each test as node}
        <Point
        x = {node.x}
        y = {node.y}
        radius = 8
        />
        {/each}

      </Graphic>


    <style>
    </style>