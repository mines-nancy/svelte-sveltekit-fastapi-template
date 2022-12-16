<script>
    import PageLayout from "$lib/layout/PageLayout.svelte"
    import EachBlockBinding from "$lib/components/EachBlockBinding.svelte"

</script>


<PageLayout>
    <div slot="main-block-content">
        <p style="text-align: center;">Contact Center</p>
        <EachBlockBinding/>
    </div>
    <div slot="left-menu-content">
        <p style="text-align: center;">Contact Left</p>
    </div>
    <div slot="right-menu-content">
        <p style="text-align: center;">Contact Right</p>
    </div>
</PageLayout>