<script>

import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
import { regressionLinear } from 'd3-regression'
import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
import DataContainer from '@snlab/florence-datacontainer'

 export let DC_raw
 export let width
 export let region

 let DC 
 $: DC = DC_raw.filter(row => row.dead === 1.0)
        .filter(row => row.yearofbirth != null)
        .filter(row => row.yearofdeath != null)
        .filter(row => row.leadershipage != null)
 $: yearOfBirth = DC.column('yearofbirth')
 $: yearOfDeath = DC.column('yearofdeath')
 $: leadershipAge = DC.column('leadershipage')
 $: yearsInPower = yearOfBirth.map((born, index) => yearOfDeath[index]-born - leadershipAge[index])
 $: DC.addColumn('yearsinpower', yearsInPower)


 $: regression = regressionLinear()
 .x(d => d.leadershipage)
 .y(d => d.yearsinpower)

 $: regressionLine = regression(DC.rows())
const padding = { left: 40, bottom: 40, top: 15, right: 10 }
</script>

  <Graphic 
  width={width}
  height={650}
  scaleX = {scaleLinear().domain(DC.domain('leadershipage')).nice()}
  scaleY={scaleLinear().domain(DC.domain('yearsinpower')).nice()}
  flipY
  padding = {padding}
  renderer = 'svg'
  >

    <PointLayer x={DC.column('leadershipage')} y={DC.column('yearsinpower')} opacity={0.5} />
    <Line 
      x={regressionLine.map(point => point[0])}
      y={regressionLine.map(point => point[1])}
      
    />
    <XAxis title='Leadership age'/>
    <YAxis title='Years in power'/>
  </Graphic>
  <p> The number of years in power in function of the age at which the leaders were appointed is plotted here for {region}. The linear regression shows an unexpected relationships depending on the region. R<sup>2</sup> has a value of {regressionLine.rSquared.toFixed(4)} for this region, showing that it is not a relevant linear relationship.</p>

<style>

p {margin-left: 20px;
  font-size:15px;}
</style>