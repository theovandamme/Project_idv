<script>
  import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis, PolygonLayer, fitScales,Label} from '@snlab/florence';
  import { regressionLinear } from 'd3-regression';
  import { scaleLinear, scaleBand, scaleTime, scaleOrdinal } from 'd3-scale';
  import { schemePaired } from 'd3-scale-chromatic';
  import DataContainer from '@snlab/florence-datacontainer';
  import { WorldRegions } from '/src/Helpers/WorldRegionExport.js';



  const WRegions = new DataContainer(WorldRegions);
  WRegions.setKey('COUNTRY') // set the key to the specific country
  console.log("Loaded Data:", WRegions);

  // set up scales
  const myGeoScale = fitScales(WRegions.domain('$geometry')); // 1. position
  const myColorScale = scaleOrdinal() // 2. fill color
    .domain(WRegions.domain('region'))
    .range(schemePaired);

  // 3. Mouseover behavior
  let active = '';
  $: Region = active ? (WRegions.row({key:active}))['region'] : '';

function handleMouseover(event) {
  active = event.key; // Update the active key
  // console.log("Active Key Updated:", active);
  // console.log("Loaded Data:", WRegions);
  
}
  function handleMouseout() {
    active = '' // Reset active
    // console.log("Mouseout: Active Key Reset");
  }
</script>

<div class="graph">
  <div class="main-chart">
    <Graphic>
      
     <Section
     width={800}
      height={400}
      {...myGeoScale}
      flipY
      onMouseout={handleMouseout}
    >
      <PolygonLayer
        geometry={WRegions.column('$geometry')}
        stroke={'white'}
        strokeWidth={1}
        fill={WRegions.map('region', myColorScale)}
        keys={WRegions.column('COUNTRY')}
        onMouseover={handleMouseover}
      />
      </Section>
     </Graphic>
    </div>
   
  {#if active !== ''}
  <div>
    <p> {Region}</p>
  </div>
  {/if}
</div>

<style>
  .graph {
    font-family: Arial, sans-serif;
  }
  /* .main-chart {
    position: relative;
  } */
  p {
    position:absolute;
    left: 150px;
    background: white;
    padding: 5px 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    pointer-events:fill;
  }
</style>
