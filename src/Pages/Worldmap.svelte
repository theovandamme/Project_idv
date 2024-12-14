<script>

    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis,PolygonLayer,fitScales } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime,scaleOrdinal } from 'd3-scale'
    import { schemePaired } from 'd3-scale-chromatic'
    import DataContainer from '@snlab/florence-datacontainer'
    import {WorldRegions} from '/src/Helpers/WorldRegionExport.js'

    const WRegions = new DataContainer(WorldRegions)
    console.log(WRegions)
    // set up scales

    // 1. position
   const myGeoScale = fitScales(WRegions.domain('$geometry'))
   // 2. fill color
   const myColorScale = scaleOrdinal()
    .domain(WRegions.domain('region'))
    .range(schemePaired)
</script>

<div class="graph">
  <div class="main-chart">
    <Graphic width={800} heigh={800} {...myGeoScale} flipY>
      <PolygonLayer 
        geometry={WRegions.column('$geometry')}
        stroke={'white'}
        strokeWidth={1}
        fill={WRegions.map('region', myColorScale)}
      />
    </Graphic>
  </div>
</div>

    
      <!-- <Graphic backgroundColor='green' width='700' height='700'>
    
       
      </Graphic> -->
    
    <style>
    </style>