<script>

    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    import OverviewGraph from '../Graphs/Overview_graph.svelte';
    import { pack } from 'd3-hierarchy';
    export let unique_leaders_raw
    export let progress
    export let select_page
    export let unique_leaders
    export let leader
    export let raw_data
    let width = 1000
    $: console.log(width)
    let start = false

</script>
    {#if (!start)}
    <div width={width} class='text'>
      <p>
        Numerous data is available about state leaders, their attributes, backgrounds and experience. Similar large-scale data about rebel leaders was untill recently non-existing. Have you ever wondered who the rebel leaders were? What kind of background they have and how their background influenced the conflicts in which they were fighting?
      </p>
    </div>
    <div width={width} class='button'>
      <button class='butt' on:click={()=> {start=true}}> Start </button>
    </div>
    
    {/if}
    <div bind:clientWidth={width} class= 'page'>
        {#if (start)}
        <OverviewGraph
          DC_raw = {unique_leaders}
          width = {width}
          raw_data = {raw_data}
          bind:select_page={select_page}
          bind:leader={leader}/>
        {/if}
    </div>
<style>
    .text {padding-left: 60px;
          padding-right: 5px;
          font-size: larger;}
    .button{ text-align: center;}
    .butt{font-size: large;}
    h2 {padding-left: 20px;}
    .page {width:90%;
            float: left;
          height:740px;
        }
    .worldmap {width:98%;
        height:700px;
        position: relative;
        float:left;
        padding-left: 20px;}
</style>