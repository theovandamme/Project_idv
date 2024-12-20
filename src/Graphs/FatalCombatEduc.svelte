<script>
  import { scaleLinear, scalePoint, scaleOrdinal } from 'd3-scale'
  import { schemeCategory10 } from 'd3-scale-chromatic'
  import { Section, PointLayer, XAxis, YAxis, DiscreteLegend, Label, Graphic } from '@snlab/florence'
  import DataContainer from '@snlab/florence-datacontainer'
  import { schemeSet3 } from 'd3-scale-chromatic'

  export let DC_raw
  export let width

  let unique_leaders_yup
  let scaleCombat
  let scaleEducation
  let scaleRadius
  let regionColorScale
  let padding

  // Data transformation: Mutating data for mean km_a by (combat, education)
  $: unique_leaders_yup = DC_raw.mutate({ 
    x1: r => r.combat,
    y1: r => r.education,
    size: r => r.km_a 
  })

  // Filtering out rows with missing or invalid km_a values
  $: unique_leaders_yup = DC_raw.filter(
    row => !isNaN(row.km_a)
  ) 

//   // Define unique categories for combat and education from the dataset 
//   $: uniqueCombat = ['0', '1', 'NaN']  // Combat experience categories
//   $: uniqueEducation = [...new Set(unique_leaders.domain('education'))]   // Dynamically extract education levels from dataset

  // Define scale for combat and education
  $: scaleX = scalePoint()
    .domain(unique_leaders_yup.domain('combat'))
    .padding(0.2) 

  $: scaleY = scalePoint()
    .domain(unique_leaders_yup.domain('education')) 
    .padding(0.2) 

  // Calculate the maximum km_a value to scale the circle radius
  $: maxFatalities = unique_leaders_yup.max('km_a') 

  $: scaleRadius = scaleLinear()
    .domain([0, maxFatalities])
    .range([2, 50])  // Adjust min and max size as needed

  regionColorScale = scaleOrdinal()
    .domain(DC_raw.domain('Region'))
    .range(schemeSet3) 

  padding = { left: 50, bottom: 40, top: 10, right: 10 }
</script>

<Graphic width={width} height={600}>
  <Section
    x1={0}
    x2={1}
    y1={0}
    y2={1}
    {scaleX}
    {scaleY}
    {padding}
  >

    <PointLayer
      x={unique_leaders_yup.column('x1')}
      y={unique_leaders_yup.column('y1')}
      radius={unique_leaders_yup.map('size', scaleRadius)}
      fill={unique_leaders_yup.map('Region', r => regionColorScale(r))}
      opacity={0.7}
    />

    <XAxis 
      title="Combat Experience"
      labelFormat={d => d}
      labelFont="Courier"
      titleFont="Courier"
      titleYOffset={30}
    />
    <YAxis 
      title="Education Level"
      labelFont="Courier"
      titleFont="Courier"
      titleXOffset={-30}
      labelFontSize={8}
    />

  </Section>

  <!-- Optional Label and Legend -->
  <Label
    x={0.5}
    y={0.98}
    text="Terrorism Fatalities by Combat Experience and Education"
    fontFamily="Courier"
    fontSize={18}
    fontWeight={800}
  />

  <DiscreteLegend
    x1={0.75} x2={1}
    y1={0} y2={0.25}
    yDivider={0}
    fill={regionColorScale.range()}
    labels={['No Combat', 'Combat', 'Unknown']}
    stroke="white"
    strokeWidth={2}
  />
</Graphic>