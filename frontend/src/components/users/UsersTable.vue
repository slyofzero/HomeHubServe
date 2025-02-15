<template>
  <div class="mb-4">
    <div class="d-flex justify-content-between align-items-center">
      <h4>All Users</h4>
      <RouterLink v-if="showViewAll" to="/admin/users">View All</RouterLink>
    </div>
    <div class="table-responsive mt-3">
      <table class="table table-bordered text-nowrap">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Joined On</th>
            <th>Role</th>
            <th>Status</th>
            <th></th>
          </tr>
        </thead>
        <tbody v-if="users.length > 0">
          <tr v-for="user in users" :key="user.id" class="text-capitalize">
            <td>{{ user.id }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>{{ formatUnixTimestamp(user.joined_on) }}</td>
            <td>{{ user.role }}</td>
            <td>{{ user.status }}</td>
            <td class="d-flex justify-content-center">
              <button
                @click="handleViewUserClick(user.id)"
                class="btn btn-primary btn-sm me-2"
              >
                View
              </button>
            </td>
          </tr>
        </tbody>
        <tbody v-else>
          <tr>
            <td class="text-center" colspan="6">No users</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <ViewUser
    v-if="showViewModal"
    :showModal="showViewModal"
    :user="userSelected"
    @close="showViewModal = false"
    @refreshUsers="refreshUsers"
  />
</template>

<script lang="ts" setup>
import { ViewUser } from "@/modals/user";
import { IUser } from "@/types/user";
import { formatUnixTimestamp } from "@/utils/time";
import { computed, ref } from "vue";

interface Props {
  users: IUser[];
  showViewAll?: any;
}
const { users, ...props } = defineProps<Props>();
const emit = defineEmits(["refreshUsers"]);

const showViewAll = computed(() =>
  typeof props.showViewAll === "boolean" ? props.showViewAll : true
);

const refreshUsers = () => {
  emit("refreshUsers");
};

// View Modal
const showViewModal = ref(false);
const userSelected = ref<IUser | null>();

const handleViewUserClick = (userId: number) => {
  showViewModal.value = true;
  userSelected.value = users.find(({ id }) => id === userId) as IUser;
};
</script>
