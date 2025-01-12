<script>
  import { scaleLinear, scalePoint, scaleOrdinal, scaleBand } from 'd3-scale'
  import { schemeCategory10 } from 'd3-scale-chromatic'
  import { Section, PointLayer, XAxis, YAxis, DiscreteLegend, Label, Graphic } from '@snlab/florence'
  import DataContainer from '@snlab/florence-datacontainer'
  import { schemeSet3 } from 'd3-scale-chromatic'
  import { color } from 'd3-color'


  export let DC_raw
  export let width
  export let selected_region
  export let darkenedSchemeSet3


  let unique_leaders_yup
  let scaleX
  let scaleY
  let scaleCombat
  let scaleEducation
  let scaleRadius
  let regionColorScale
  let padding

  
  let educ = ["No/incomplete primary", "Finished primary", "Finished secondary","Obtained Bachelor's", "Obtained Master's, Obtained Bachelor's","Obtained Master's","Obtained Doctorate"]


        $: unique_leaders_yup = DC_raw
            .filter(row => row.combat == "1.0" || row.combat == "0.0") 
            .filter(row => row.education != null);

        $: educ_scale = educ.filter((educ)=> unique_leaders_yup.column('education').includes(educ))


        $: unique_leaders_yep = unique_leaders_yup
            .select(['combat', 'education', 'km_a'])
            .groupBy(['education', 'combat'])
            // .filter(r => r.km_a != null && !isNaN(r.km_a))
            .summarise({ mean_km_a: {km_a: 'mean'} })

        $: combatDomain = ['0.0', '1.0']
        $: scaleCombat = scalePoint()
            .domain(unique_leaders_yep.domain('combat'))
            .padding(0.7)

        $: educationDomain = ["No/incomplete primary", "Finished primary", "Finished secondary","Obtained Bachelor's", "Obtained Master's, Obtained Bachelor's","Obtained Master's","Obtained Doctorate"]
        $: scaleEducation = scalePoint()
            .domain(educationDomain)
            .padding(0.2) 

        $: maxMeanKma = unique_leaders_yep.max('mean_km_a') 
        $: scaleRadius = scaleLinear()
            .domain([0, maxMeanKma])
            .range([3, 42])
        
        $: console.log(unique_leaders_yep)
        
        

        // $: scaleX = scalePoint() 
        //     .domain(unique_leaders_yup.domain('combat'))
        //     .padding(0.75) 

        // $: scaleY = scalePoint()
        //     .domain(unique_leaders_yup.domain('education')) 
        //     .padding(0.4) 

        // // Calculate the maximum km_a value to scale the circle radius
        // $: maxMeanFatalities = unique_leaders_yup.max('mean_km_a') 

        // $: scaleRadius = scaleLinear()
        //     .domain([0, maxMeanFatalities])
        //     .range([2, 50])

  regionColorScale = scaleOrdinal()
    .domain(DC_raw.domain('Region'))
    .range(darkenedSchemeSet3) 

  padding = { left: 200, bottom: 40, top: 10, right: 10 }
</script>

<Graphic width={width} height={600}>
  <Section
    x1={0}
    x2={1}
    y1={0}
    y2={0.9}
    scaleX = {scaleCombat}
    scaleY = {scaleEducation}
    {padding}
    flipY
  >

    <!-- <PointLayer
      x={unique_leaders_yup.column('combat')}
      y={unique_leaders_yup.column('education')}
      radius={unique_leaders_yup.map('mean_km_a', scaleRadius)}
      fill={unique_leaders_yup.map('Region', r => regionColorScale(r))}
      opacity={0.7}
    /> -->
    <PointLayer
    x={unique_leaders_yep.column('combat')}
    y={unique_leaders_yep.column('education')}
    radius={unique_leaders_yep.map('mean_km_a', scaleRadius)}
    fill={DC_raw.map('Region', row => row === selected_region ? regionColorScale(row) : "#3D3D3D")}
    stroke='grey'
    fillOpacity={0.8}

    
    />

    <XAxis 
      title="Combat Experience"
      labelFormat={d => d === 1.0 ? "Yes" : "No"}
      labelFont="Courier"
      titleFont="Courier"
      titleYOffset={30}
    />
    <YAxis 
      title="Education Level"
      labelFont="Courier"
      titleFont="Courier"
      titleXOffset={-120}
      labelFontSize={8}
    />

  </Section>

  <Label
    x={0.55}
    y={0.95}
    text="Mean Terrorism Fatalities by Combat Experience and Level of Education"
    fontFamily="Courier"
    fontSize={18}
    fontWeight={600}
  />

  <!-- <DiscreteLegend
    x1={0.75} x2={1}
    y1={0} y2={0.25}
    yDivider={0}
    fill={regionColorScale.range()}
    stroke="white"
    strokeWidth={2}
  /> -->
  <!-- <YGridLines opacity = {0.5} />
  <XGridLines opacity = {0.5} />
   -->
</Graphic>