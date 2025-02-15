<template>
  <Modal :show-modal="props.showModal">
    <!-- Modal Header -->
    <template #header>
      <div class="modal-header border-0">
        <h4 class="modal-title w-100 text-center">User Profile</h4>
        <button
          @click="closeModal"
          class="btn-close"
          aria-label="Close"
        ></button>
      </div>
    </template>

    <!-- Modal Body -->
    <template #body>
      <div class="d-flex flex-column gap-4">
        <span
          v-if="errorMessage"
          class="text-danger bg-danger-subtle rounded px-4 py-1"
          >{{ errorMessage }}</span
        >

        <div class="modal-body d-flex flex-column gap-2 text-capitalize">
          <div class="d-flex gap-2">
            <span>Name</span> -
            <span>{{ user?.name }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Email</span> -
            <span>{{ user?.email }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Pincode</span> -
            <span>{{ user?.pincode }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Role</span> -
            <span>{{ user?.role }}</span>
          </div>
          <div class="d-flex gap-2">
            <span>Joined On</span> -
            <span
              >{{ formatUnixTimestamp(user?.joined_on) }} ({{
                timeSince(user.joined_on)
              }})</span
            >
          </div>
          <AccountStatus :account="user" />
        </div>

        <form v-if="userStore.isAdmin" @submit.prevent="() => {}">
          <!-- Modal Footer -->
          <div class="d-flex justify-content-center gap-3 flex-wrap">
            <button
              @click="applicationAction('BLOCKED')"
              class="btn btn-success px-4"
              v-if="user.status === 'ALLOWED' && userStore.isAdmin"
            >
              Block
            </button>

            <button
              @click="applicationAction('BLOCKED')"
              class="btn btn-success px-4"
              v-if="user.status === 'BLOCKED' && userStore.isAdmin"
            >
              Unblock
            </button>

            <button
              type="button"
              class="btn btn-secondary px-4"
              @click="closeModal"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </template>
  </Modal>
</template>

<script lang="ts" setup>
import { clientPoster } from "@/utils/api";
import { IApiRes, IUser } from "@/types";
import { ref } from "vue";
import { formatUnixTimestamp, timeSince } from "@/utils/time";
import Modal from "../Modal.vue";
import { useUserStore } from "@/stores";
import { AccountStatus } from "@/components/utils";

const props = defineProps<{
  showModal: boolean;
  user: IUser | null;
}>();

const emit = defineEmits(["close", "refreshUsers"]);
const errorMessage = ref("");
const userStore = useUserStore();

// Action functions
async function closeModal() {
  emit("close");
}
async function applicationAction(status: IUser["status"]) {
  const url = `${import.meta.env.VITE_API_URL}/admin/user/${props.user?.id}`; // prettier-ignore
  const res = await clientPoster<IApiRes>(url, { status });
  if (res.response === 200) {
    closeModal();
    errorMessage.value = "";
    emit("refreshUsers");
  } else {
    errorMessage.value = res.data.message || "Couldn't delete profile.";
  }
}
</script>
