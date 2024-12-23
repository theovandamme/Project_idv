<script>

    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis, x2s } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime, scaleOrdinal } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    export let DC_raw
    export let width
    export let darkenedSchemeSet3
    export let selected_region
    
    let DC
    let education_DC
    let regionColorScale
    let educ = ["No/incomplete primary", "Finished primary", "Finished secondary","Obtained Bachelor's", "Obtained Master's, Obtained Bachelor's","Obtained Master's","Obtained Doctorate"]
   

    $: if (DC_raw.column('Region')[0] != 'Oceania') {
      DC = new DataContainer({education: DC_raw.column('education'), educwest: DC_raw.column("educwest")})
      education_DC = DC.dropNA().groupBy('education')}
    const padding = { left: 40, bottom: 50, top: 5, right: 10 }

    $: educ_scale = educ.filter((educ)=> education_DC.column('education').includes(educ))

    regionColorScale = scaleOrdinal()
            .domain(DC_raw.domain('Region'))
            .range(darkenedSchemeSet3);

    
    </script>
      {#if (DC_raw.column('Region')[0] != 'Oceania')}
      <Graphic  width={width} height='650'
      scaleX = {scaleBand().domain(educ_scale).padding(0.1).paddingOuter(0.5)}
      scaleY = {scaleLinear().domain([0,Math.max(1,...education_DC.column('$grouped').map((x)=> x.nrow()|| 0))]).nice()}
      flipY
      {padding}>
        
        <RectangleLayer

        x1 = {education_DC.column('education')}
        x2 = {x2s(education_DC.column('education'))}
        y1 = {education_DC.map('education', x => 0 )}
        y2 = {education_DC.column('$grouped').map((x)=> x.nrow()|| 0)}
        fill = {DC_raw.map('Region', row => row === selected_region ? regionColorScale(row) : "#3D3D3D")}/>
        <XAxis 
        labelOffset = '15'
        labelRotate= '-0.2'
        />
        <YAxis
        title='Frequency'
        />
      </Graphic>
      {:else}
      <h3> This chart is not availble for Oceania</h3>
      {/if}
    <style>
    </style>