<script>

    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis, x2s } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    export let DC_raw
    export let width
    
    let DC
    let education_DC
    let educ = ["No/incomplete primary", "Finished primary", "Finished secondary","Obtained Bachelor's", "Obtained Master's, Obtained Bachelor's","Obtained Master's","Obtained Doctorate"]
   

    $: if (DC_raw.column('Region')[0] != 'Oceania') {
      DC = new DataContainer({education: DC_raw.column('education'), educwest: DC_raw.column("educwest")})
      education_DC = DC.dropNA().groupBy('education')}
    const padding = { left: 40, bottom: 50, top: 5, right: 10 }

    $: educ_scale = educ.filter((educ)=> education_DC.column('education').includes(educ))

    
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
        fill = {'green'}/>
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