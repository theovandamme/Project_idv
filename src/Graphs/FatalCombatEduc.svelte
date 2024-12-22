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

  let educ = ["No/incomplete primary", "Finished primary", "Finished secondary","Obtained Bachelor's", "Obtained Master's, Obtained Bachelor's","Obtained Master's","Obtained Doctorate"]

  function safeMean(values) {
    const validValues = values.filter(v => v != null && !isNaN(v));
    return validValues.length > 0 ? validValues.reduce((a, b) => a + b) / validValues.length : null;
  } 

        $: unique_leaders_yup = DC_raw
            .filter(row => row.combat == "1.0" || row.combat == "0.0") 
            .filter(row => row.education != null);

        $: educ_scale = educ.filter((educ)=> unique_leaders_yup.column('education').includes(educ))


        $: unique_leaders_yup = unique_leaders_yup
            .select(['combat', 'education', 'km_a'])
        $: unique_leaders_yup = unique_leaders_yup
            .groupBy(['education', 'combat'])
            .filter(r => r.km_a != null && !isNaN(r.km_a))
            .summarize({ mean_km_a: d => safeMean(d.km_a) })

        $: console.log(unique_leaders_yup)

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

  // regionColorScale = scaleOrdinal()
  //   .domain(DC_raw.domain('Region'))
  //   .range(schemeSet3) 

  padding = { left: 200, bottom: 40, top: 10, right: 10 }
</script>

<Graphic width={width} height={600}>
  <!-- <Section
    x1={0}
    x2={1}
    y1={0}
    y2={1}
    {scaleX}
    {scaleY}
    {padding}
  > -->

    <!-- <PointLayer
      x={unique_leaders_yup.column('combat')}
      y={unique_leaders_yup.column('education')}
      radius={unique_leaders_yup.map('mean_km_a', scaleRadius)}
      fill={unique_leaders_yup.map('Region', r => regionColorScale(r))}
      opacity={0.7}
    /> -->

    <!-- <XAxis 
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
    /> -->

  <!-- </Section> -->

  <!-- <Label
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
    stroke="white"
    strokeWidth={2}
  /> -->
</Graphic>