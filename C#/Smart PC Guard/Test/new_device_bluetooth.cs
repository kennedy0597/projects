using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using InTheHand.Net.Sockets;
using System.Diagnostics;

namespace Test
{
    public partial class new_device_bluetooth : Form
    {

        public string ReturnText { get; set; }
        public new_device_bluetooth()
        {
            InitializeComponent();


        }

        System.Windows.Forms.Form f = System.Windows.Forms.Application.OpenForms["login"];
       
        private void New_device_Load(object sender, EventArgs e)
        {

        }


        public string BTdevice{ get; set; }
        
        private void Button3_Click(object sender, EventArgs e)
        {
            BluetoothDeviceInfo[] devices;
            using (BluetoothClient sdp = new BluetoothClient())
                devices = sdp.DiscoverDevices();

            foreach (BluetoothDeviceInfo deviceInfo in devices)
            {
                checkedListBox1.Items.Add(string.Format("{0} ({1})", deviceInfo.DeviceName, deviceInfo.DeviceAddress));
                
            }

        }

        private void CheckedListBox2_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void CheckedListBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }



        private void CheckedListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void CheckedListBox1_SelectedIndexChanged_1(object sender, EventArgs e)
        {

        }

        private void Button4_Click(object sender, DataReceivedEventArgs e)
        {

        }

        private void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }
        
        private void Button4_Click(object sender, EventArgs e)
        {
            foreach (object itemChecked in checkedListBox1.CheckedItems)
            {
                this.ReturnText = this.textBox1.Text;
                textBox1.Text += itemChecked.ToString();
                textBox2.Text += itemChecked.ToString();
                BTdevice = textBox2.Text;

            }
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            
            Main main = new Main(textBox1.Text);

            main.ShowDialog();
            this.Close();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            Main main = new Main();
            main.Show();
            this.Close();
        }

        
    }
}
