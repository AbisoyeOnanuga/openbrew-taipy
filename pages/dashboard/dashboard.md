# **Brewery Dashboard**{: .color-primary} Information

<|{selected_brewery}|selector|lov={selector_brewery}|on_change=on_change_brewery|dropdown|label=Brewery Name|>

<br/>

<|layout|columns=1 1 1|gap=50px|
<|card|
**Brewery Name**{: .color-primary}
<|{data_brewery.iloc[0]['Name']}|text|class_name=h2|>
|>

<|card|
**Brewery Type**{: .color-primary}
<|{data_brewery.iloc[0]['Type']}|text|class_name=h2|>
|>

<|card|
**Location**{: .color-primary}
<|{data_brewery.iloc[0]['Street']}, {data_brewery.iloc[0]['City']}, {data_brewery.iloc[0]['State']}|text|class_name=h2|>
|>
|>

<br/>
<br/>

<|layout|columns=1 1 1|gap=50px|
<|card|
**Contact**{: .color-primary}
<|{data_brewery.iloc[0]['Phone']}|text|class_name=h2|>
|>

<|card|
**Website**{: .color-primary}
<|{data_brewery.iloc[0]['Website Link']}|text|class_name=h2|>
|>

<|card|
**Google Maps**{: .color-primary}
<|{data_brewery.iloc[0]['Google Maps Link']}|text|class_name=h2|>
|>
|>
