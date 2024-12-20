<script>
  import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis, PolygonLayer, fitScales,Label} from '@snlab/florence';
  import { regressionLinear } from 'd3-regression';
  import { scaleLinear, scaleBand, scaleTime, scaleOrdinal } from 'd3-scale';
  import { schemePaired,schemeSet3 } from 'd3-scale-chromatic';
  import DataContainer from '@snlab/florence-datacontainer';
  import { WorldRegions } from '/src/Helpers/WorldRegionExport.js';



  const WRegions = new DataContainer(WorldRegions);
  WRegions.setKey('COUNTRY') // set the key to the specific country
  console.log("Loaded Data:", WRegions);

  // set up scales
  const myGeoScale = fitScales(WRegions.domain('$geometry')); // 1. position
  const myColorScale = scaleOrdinal() // 2. fill color
    .domain(WRegions.domain('region'))
    .range(schemeSet3);

    
  // 3. Mouseover behavior
  let active = '';
  let RegionData
  $: Region = active ? (WRegions.row({key:active}))['region'] : ''
  $:if (active !== ''){
    RegionData=WRegions.filter(row=>row.region === Region)
    console.log(RegionData)
  } else {
    RegionData = WRegions
  }


function handleMouseover(event) {
  active = event.key; // Update the active key

function handleClick(event){
}
  
}
  function handleMouseout() {
    active = '' // Reset active
    // console.log("Mouseout: Active Key Reset");
  }
</script>

  <div class="main-chart">
    <Graphic width={500} height={200} backgroundColor={'blue'} {...myGeoScale}
      flipY>
      <PolygonLayer
        geometry={WRegions.column('$geometry')}
        stroke={'white'}
        strokeWidth={1}
        fill={WRegions.map('region', myColorScale)}
        keys={WRegions.column('COUNTRY')}
        onMouseover={handleMouseover}
        onMouseout={handleMouseout}
      />
      <!-- trying to add the selected region on top  -->
      {#if active !== ''}
      <PolygonLayer
      geometry={RegionData.column('$geometry')}
      strokeWidth={5}
      fill={'red'} />  
          
      {/if}
     </Graphic>
    </div>
  {#if active !== ''}
    <div>
    <p> {Region}</p>
  </div>
  {/if}

<style>
  .graph {
    font-family: Arial, sans-serif;
  }

  p {
    position:absolute;
    top: 200px;

    left: 450px;
    background: white;
    padding: 5px 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    pointer-events:fill;
  }
</style>
