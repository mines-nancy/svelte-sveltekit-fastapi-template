<script>
    import PageLayout from "$lib/layout/PageLayout.svelte"
    import NumericInputs from "$lib/components/NumericInputs.svelte"
</script>


<PageLayout>
    <div slot="main-block-content">
        <p style="text-align: center;">Home Center</p>
        <NumericInputs/>
    </div>
    <div slot="left-menu-content">
        <p style="text-align: center;">Home Left</p>
    </div>
    <div slot="right-menu-content">
        <p style="text-align: center;">Home Right</p>
    </div>
</PageLayout>