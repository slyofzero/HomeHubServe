<template>
  <!-- Modal -->
  <div
    v-if="showModal"
    class="modal fade show"
    tabindex="-1"
    style="display: block"
    aria-modal="true"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content p-4">
        <!-- Modal Header -->
        <slot name="header" />

        <!-- Modal Body -->
        <slot name="body" />
      </div>
    </div>
  </div>

  <!-- Custom Backdrop -->
  <div
    v-if="showModal"
    style="
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      z-index: 1040;
    "
  />
</template>

<script lang="ts" setup>
const { showModal } = defineProps({
  showModal: {
    type: Boolean,
    required: true,
  },
});
</script>
