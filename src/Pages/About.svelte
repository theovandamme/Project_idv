<script>
    let value =''
    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'

    
    $: console.log(value)
    </script>
      <input type="text" placeholder="Search" bind:value/>
      <Graphic backgroundColor='green' width='700' height='700'>
    
       
      </Graphic>
    
    <style>
    </style>